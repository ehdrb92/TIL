# 접속 유저 IP 수집 View 작성

```python
from django.views import View
from django.http  import JsonResponse

from users.models import User

class CheckVisitor(View):
    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        if not User.objects.filter(user_ip=ip):
            User.objects.create(user_ip=ip)

        visitors = User.objects.all()

        result = [{
            'user_ip' : visitor.user_ip,
            'created_at' : visitor.created_at,
            'updated_at' : visitor.updated_at
        }for visitor in visitors]

        return JsonResponse(result, status = 200, safe=False)
```

위 코드는 장고에서 유저 ip를 받아 데이터베이스에 저장하는 법에 대해 구글링하여 나온 stackoverflow의 코드를 긁어와 조금 수정한 것이다

코드들의 의미를 하나하나 뜯어보자

`request.META`는 "Django 서버로 전송되는 HTTP 요청의 모든 메타데이터를 포함하며, 사용자 에이전트, IP 주소, 콘텐츠 유형 등을 포함할 수 있다." 라고 한다.

헤더가 비어있으면 KeyError가 발생하기 때문에 항상 예외처리를 만들어 주는 편이 좋다고 한다.

그러면 해당 메타데이터에서 받아올 `HTTP_X_FORWARDED_FOR`는 무엇일까??

이를 말하기 전에 먼저 `REMOTE_ADDR`가 선행으로 설명되는게 맞을 것같다. `REMOTE_ADDR`는 찾아본 결과 다음과 같다.

* 현재 페이지를 보고 있는 사용자의 IP 주소를 담은 PHP 환경변수
* 서버 앞단에 프록시가 없는 경우, 클라이언트의 IP 주소
* 서버 앞단에 프록시가 있는 경우, 프록시로 돌아가는 IP 주소

다음으로 `HTTP_X_FORWARDED_FOR`이다. 앞의 `HTTP_`는 HTTP 헤더의 내용을 받아올 때 앞에 붙여주어야 되는 수식어?? 같은 것이라고 이전에 배웠다. 그렇다면 뒤에 `X_FORWARDED_FOR`는 무엇일까??

이는 줄여서 `XFF`라고 부른다고 한다. 해당 HTTP 헤더는 클라이언트가 프록시 서버를 통해 페이지에 접속해 올 때도 클라이언트의 정확한 IP를 받아올 수 있어 이를 쓴다고 한다.

그리고 이를 받아 왔을 때 `,`를 기준으로 배열의 마지막 것만 가져오는 코드가 있는데, 이는 주소가 다음과 같이 전송되기 때문이다.

```terminal
# X-Forwarded-For: client, proxy1, proxy2

X-Forwarded-For: 203.0.113.195, 70.41.3.18, 150.172.238.178
X-Forwarded-For: 203.0.113.195
X-Forwarded-For: 2001:db8:85a3:8d3:1319:8a2e:370:7348
```

이 이상 자세한 것은 따로 정리해보도록 해야겠다.

이후 코드는 보면 바로 알다 싶이 해당 ip를 받아와 `users`테이블의 데이터로 저장하는 과정이다.

`XFF` 위키백과 : https://en.wikipedia.org/wiki/X-Forwarded-For

`proxy` 위키백과 : https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9D%EC%8B%9C_%EC%84%9C%EB%B2%84 