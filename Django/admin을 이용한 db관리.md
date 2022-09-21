# admin앱을 이용한 장고 데이터베이스 관리

장고 기본에서 지원하는 admin은 몇 가지 설정만으로 데이터베이스 테이블 CRUD (생성, 조회, 수정, 삭제) 기능을 제공해주는 툴이다.

하지만 이는 어느정도의 한계가 있고, 개발 초기 단계에서 데이터베이스를 관리하기에 좋다.

admin은 데이터베이스 테이블 데이터 관리툴 정도로만 보고, 보다 전문적인 관리자 툴이 필요하시다면 직접 구현이 필요하다.

## 모델 클래스 등록하기

`앱 이름/admin.py`에 아래의 코드를 입력한다.

```python
from django.cotrib import admin
from .models import {모델명}

# 1. 기본 ModelAdmin 동작

admin.site.register({모델명})

# 등록한 모델을 해지하려면 unregister라는 함수를 사용한다.

# 2. 지정한 ModelAdmin 동작

class {모델명}Admin(admin.ModelAdmin):
        pass

admin.site.register({모델명}, {모델명}Admin)

# 3. 데코레이터를 이용

@admin.register({모델명})
class {모델명}Admin(admin.ModelAdmin):
    pass
```

## __str__ 구현

admin 관리 페이지에서 기본적으로 데이터들은 `모델명 object`값으로 표현된다.

이를 관리자가 보고싶은 표현방식으로 변경하는 것이 **__str__**이다.

```python
from django.db import models

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        # return f"Custom Post object ({self.id})"
        return self.message
```

위와 같은 방식으로 __str__을 정의하면 해당 테이블의 message 데이터가 표시된다.

## list display 속성 정의

list display 속성을 이용하여 관리 페이지에서 보고싶은 데이터를 볼 수 있다.

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']
```

위처럼 list_display 배열을 통해 관리 페이지에 보여주고 싶은 값들을 정의해줄 수 있다.

그리고 기본적으로 해당 데이터의 상세 정보를 보는 link는 pk값에 있다.

하지만 list_display_links 배열에 특정 속성을 넣어주면 해당 속성에 링크가 연결된다.

다음으로 위 list_display를 보면 `message_length`라는 모델에 정의되지 않은 데이터가 보인다.

이는 실제로 존재하지는 않지만 특정 코드를 통해 보여주고 싶은 값을 지정해 줄 수 있다.

먼저 앱의 model.py에서 정의하는 방법이다.

```python
    def message_length(self):
        return len(self.message)
    message_length.short_description = '메세지 글자수'
```

위의 코드를 모델 클래스 하단에 정의하면 message속성의 길이값을 보여주는 칼럼을 추가할 수 있다.

이는 admin.py에서도 구현이 가능하다.

## search_field 속성 정의하기

search_field 속성을 정의하여 관리 페이지 내에서 검색 UI를 만들 수 있다.

이는 데이터베이스 내에서 WHERE 쿼리문의 기능을 사용한다.

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']
    search_fields = ['message']
```

admin.py의 정의된 클래스 하단에 search_field를 추가하고, 검색하고싶은 칼럼을 넣어준다.

해당 코드를 넣어주면 관리 페이지에 검색 UI가 생성된다.

그리고 배열에 넣어준 칼럼 속성에 한해 검색기능을 제공한다.

## list_filter 속성 정의하기

list_filter 속성을 이용하여 필터기능을 추가하는 방법이다.

```python
# model.py

class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# admin.py

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
```

위의 코드를 적용시켜 주면 관리 페이지의 오른쪽 편에 지정해준 칼럼들에 대해 필터 옵션이 추가된다.
