# CASCADE 옵션의 작동방식에 대해

2차 프로젝트의 완성본을 배포하려고 테스트를 하던 중 오류가 발생하였다.

게시글의 댓글을 조회하는 부분이었는데, 로그인 검증을 하기위해 걸어두었던 예외처리 오류가 발생한 것이다.

코드는 다음과 같다.

```python
import jwt

from django.conf  import settings
from django.http  import JsonResponse

from users.models import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('AUTHORIZATION')

            if access_token == '':
                request.user = None
                return func(self, request, *args, **kwargs)

            payload      = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id=payload['id'])

            return func(self, request, *args, **kwargs)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE':'INVALID_PAYLOAD'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
    
    return wrapper
```

여기서 우리의 기획대로라면 로그인하지 않은 상태의 클라이언트 또한 댓글의 조회는 가능해야 했기에 로그인 하지않았을 경우 요청의 헤더에 있는 `'AUTHORIZATION'`를 공백으로 두기로 하였다.

이후 url과 헤더 부분을 모두 체크하고 정확하게 요청을 보냈는데 계속해서 `{'MESSAGE':'INVALID_USER'}`가 발생하였다.

분명히 공백으로 두면 해당 코드가 작동 할 수가 없다.... 왜냐하면 해당 예외가 발생하는 것은 `request.user = User.objects.get(id=payload['id'])`부분에서 디코딩을 했는데 없는 유저의 id가 들어가 있어야 하기 때문이다.

그래서 해당 부분까지 코드가 흘러갔는지 확인하기 위해 중간중간에 print를 심어 경과를 확인하였지만 코드는 해당 부분으로 분기된적이 없다.....

계속해서 원인을 찾지 못하다가 정확한 디버그를 확인하기 위해 예외처리 부분을 주석처리하고 다시 실행해보았다.

그런데 문제는 엉뚱한 곳에서 발생하였다. 바로 댓글을 불러오는 부분이었다. 해당 로직의 코드는 다음과 같다.

```python
    @login_decorator
    def get(self, request, post_id):
        user   = request.user
        limit  = int(request.GET.get('limit', 5))
        offset = int(request.GET.get('offset', 0))

        comments_total = Comment.objects.filter(post=post_id).count()
        comments       = Comment.objects.filter(post=post_id, parent_comment_id=0).order_by('-created_at')

        user_id = None
        if not user == None:    
            user_id = user.id

        result = []

        for comment in comments:
            result.append({
                'id'               : comment.id,
                'user_id'          : comment.user_id,
                'parent_comment_id': comment.parent_comment_id,
                'profile_image_url': comment.user.profile_image_url, # 문제 발생 부분
                'nickname'         : comment.user.nickname,
                'comment'          : comment.comment,
                'created_at'       : comment.created_at,
                'depth'            : 0
            })
            for review in Comment.objects.filter(parent_comment_id=comment.id).order_by('-created_at'):
                result.append({
                    'id'               : review.id,
                    'user_id'          : review.user_id,
                    'parent_comment_id': review.parent_comment_id,
                    'profile_image_url': review.user.profile_image_url,
                    'nickname'         : review.user.nickname,
                    'comment'          : review.comment,
                    'created_at'       : review.created_at,
                    'depth'            : 1
                })

        result_res = {'comment' : result[offset : offset + limit]}

        result_res['user_id']        = user_id
        result_res['comments_total'] = comments_total

        return JsonResponse(result_res, status = 200, safe=False)
```

댓글 작성자의 프로필 사진을 불러오는 부분에서 해당 유저가 없어 User.DoesNotExist가 발생한 것이다....

그런데 위 코드에서 보면 알듯이 해당 view에는 해당 예외처리를 하지 않았다.

그런데도 예외처리가 해당 오류로 인해 발생했다는 것은 데코레이터 내부에 처리한 예외처리 또한 데코레이터의 영향을 받는 코드 로직에서 또한 작동한다는 사실이다.

이 부분은 새로이 알게 되었다.....

그런데 또한 뭔가 의문이 생겼다. 일단은 댓글의 모델링 코드이다.

```python
from django.db    import models

from core.models  import TimeStampModel
from users.models import User
from posts.models import Post

class Comment(TimeStampModel):
    post              = models.ForeignKey(Post, on_delete=models.CASCADE)
    user              = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment_id = models.IntegerField()
    comment           = models.TextField()

    class Meta:
        db_table = 'comments'
```

보면 알겠지만 댓글을 작성한 유저의 정보가 데이터베이스에서 삭제되면 해당 댓글 또한 삭제되도록 `CASCADE`옵션을 걸어두었다.

그러면 해당 유저를 탈퇴시켜 정보가 유저 테이블상에서 삭제되었는데도 해당 댓글이 삭제되지 않고 살아있는다는 것인데.....

그렇다면 CASCADE 옵션이 하나의 데이터에 두 갈래로 붙어있다면 해당하는 두 가지 데이터가 모두 삭제되어야만 역참조되는 데이터가 사라진다는 말인가???