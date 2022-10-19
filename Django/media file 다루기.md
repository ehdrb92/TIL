# 장고에서 미디어 파일 다루기

장고에서 미디어 파일을 다루는 방법에 대해 알아보자

## Static 파일과 Media 파일

**Static 파일**이란 개발 리소스로서 정적인 파일 (css, js 등...)

앱, 프로젝트 단위로 저장/서빙

**Media 파일**이란 FileField/ImageField로 저장된 모든 파일 스토리지에 파일이 저장되며 데이터베이스에 해당 스토리지의 경로를 저장한다. 프로젝트 단위로 저장/서빙

## Pillow 라이브러리

파이썬 장고에서 ImageField를 사용하기 위해서는 **pillow**라이브러리가 필요하다.

`pip install pillow`

## 장고에서 media 파일의 처리 순서

1. HttpRequest.FILES를 통해 파일이 전달
2. 뷰, 폼 로직을 통해 유효성 검증
3. FileField, ImageField에 경로(문자열)저장
4. settings.MEDIA_ROOT 경로에 파일 저장

## 미디어 파일저장 경로 설정

`settings.py`로 이동해서 아래의 환경변수를 추가한다.

```python
MEDIA_URL = ‘/media/’
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

만약 MEDIA_ROOT를 설정하지 않으면 프로젝트의 root 디렉토리에 이미지 파일이 저장된다.

## FileField와 ImageField

FileField는 File Storage API를 통해 파일을 저장한다.

해당 필드를 옵션으로 두고자 하면 `blank=True`속성을 추가한다.

ImageField는 Pillow 라이브러리를 통해 이미지의 width/height를 얻어 이미지를 저장한다.

## upload_to 옵션

settings.MEDIA_ROOT 하위에서 저장한 파일명/경로명 결정

디폴트 : 파일명 그대로 settings.MEDIA_ROOT 에 저장

동일 파일명으로 저장 시에, 파일명에 더미 문자열을 붙여 파일 덮어쓰기 방지

```python
upload_to="instagram/post/%Y/%m/%d"
```

위와 같이 코드를 입력해주면, instagram/post 하위 디렉토리에

년(4자리)/월(2자리)/일(2자리)로 디렉토리가 생성되고 해당 디렉토리에 파일이 저장된다.

## uuid를 이용하여 저장되는 파일의 이름 수정하기

본래 미디어 파일을 저장하면 파일명 그대로 저장된다.

하지만 보통 여러가지 이유에서 서버에 파일명 그대로 저장하는 경우는 거의 없다.

그래서 난수값을 가져오는 uuid를 이용하여 파일명을 수정하여 저장할 수 있다.

```python
import os
from uuid import uuid4
from django.utils import timezone
def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label # 앱 별로
    cls_name = instance.__class__.__name__.lower() # 모델 별로
    ymd_path = timezone.now().strftime('%Y/%m/%d’) # 업로드하는 "년/월/일" 별로
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환 
    return '/'.join([
        app_label,
        cls_name,
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,
    ])
```

## 개발 환경에서 파일의 url 서빙하기

static 파일과 다르게, 장고 개발서버에서 서빙 미지원

개발 편의성 목적으로 직접 서빙 Rule 추가 가능

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
