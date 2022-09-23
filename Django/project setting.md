# 장고 프로젝트 초기세팅

장고 프로젝트를 시작하기 뮈한 초기세팅 정리

## 가상환경 생성

특정 프로젝트의 성격에 맞게 파이썬 버전 및 패키지 등의 세팅값을 설정해놓기 위한 가상환경을 생성.

```terminal
conda create -n [가상환경명] python=3.9 -> 가상환경 생성

conda activate [가상환경명] -> 가상환경 가동

conda deactivate -> 가상환경 헤제
```

## 데이터베이스 생성

프로젝트에서 사용할 데이터베이스 생성

```mysql
mysql> create database [데이터베이스명] character set utf8mb4 collate utf8mb4_general_ci;
```

utf8mb4            : 한글을 포함한 전세계 문자 + 이모티콘 사용 가능
utf8mb4_general_ci : 가장 정확하지는 않지만 정렬 속도 빠름

## 필요 패키지 설치

장고 프로젝트를 하기위해 장고 프레임워크 설치

```terminal
pip install django -> 장고 프레임워크 설치

pip install mysqlclient -> python과 mysql 서버와 연결하여 각종 명령어를 사용하게 해주는 패키지

pip install django-cors-header -> django에 cors 옵션 추가

pip install django-extensions ipython -> django python shell을 편하기 사용하기 위한 패키지
```

## 프로젝트 생성

프로젝트를 생성하기 전 해당 디렉토리를 직접 만드는 방법이 더 좋다.

'''terminal
django-admin startproject [프로젝트명] . (마지막 '.'은 자신이 현재 있는 디렉토리에 프로젝트를 생성한다는 의미이다. 없으면 프로젝트명으로된 디렉토리를 생성하고 그곳에 프로젝트가 생성된다.)
'''

## 프로젝트 서버 동작 확인

프로젝트의 서버가 정상적으로 작동하는지 점검한다.

```terminal
python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 15, 2022 - 06:01:05
Django version 4.0.6, using settings 'westagram.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

서버가 정상적으로 동작 시 위와 같은 메세지 출력
```

## 프로젝트 앱 생성

프로젝트에서 사용할 앱을 생성

```terminal
python manage.py startapp [앱명]
```

## settings.py 설정

프로젝트를 진행하면서 각종 설정을 진행한다.

### settings.py

```python
from pathlib     import Path

from my_settings import DATABASES, SECRET_KEY

BASE_DIR = Path(__file__).resolve().parent.parent

##### Check Point 1.환경변수 관리
SECRET_KEY = my_settings.SECRET_KEY

DEBUG = True

##### Check Point 2.ALLOWED_HOSTS에 IP 명시했는가? 기본 '*'
ALLOWED_HOSTS = ['*']

##### Check Point 3.Admin App 사용 해제
INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

##### Check Point 4.Admin 관련 middleware 사용 해제 & corsMiddelware 추가
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
WSGI_APPLICATION = 'westagram.wsgi.application'
ROOT_URLCONF     = 'westagram.urls'
TEMPLATES        = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ], },
    },
]

##### Check Point 5. Database setting 환경변수로 관리
DATABASES = DATABASES

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True
STATIC_URL    = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APPEND_SLASH = False

##### Check Point 6. CORS 설정
CORS_ORIGIN_ALLOW_ALL  = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS     = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
```

### my_settings.py

```python
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '[데이터베이스명]',
        'USER': '[서버명]',
        'PASSWORD': '[데이터베이스 패스워드]',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}
        
SECRET_KEY = 'django-insecure-u$g22)0c&)(p#)!v0$ht6u=2ge^263v&y1r&b(5i*2s+&5ppch'
```

데이터베이스와 시크릿키에 대한 환경변수를 따로 빼서 관리하기 위해 `my_settings.py`파일을 별도로 생성하여 넣어두었다.

추후에 jwt를 발급할 때 알고리즘과 같은 환경변수도 모두 이곳에서 관리할 수 있다.

## .gitignore

git을 통해 커밋을 할 때 해당 파일의 리스트에 있는 파일은 커밋되지 않는다.

노출시키기 싫은 정보를 해당 파일에 추가하면 된다.

[https://www.toptal.com/developers/gitignore]

위 사이트에서 키워드 키워드만 입력해주면 해당 관련된 리스트를 자동으로 뽑아주니 사용하여 나온 텍스트를 모두 복붙하도록하자.

그리고 환경변수를 관리하기 위해 `my_setting.py` 또한 포함시킨다.

## requirements.txt

설치된 파이썬 패키치를 확인하고 관리하기 위해 만들어 준다.

특정한 기능을 하는 것은 아니다. 여러명과 협업을 하게되었는데 만약 설치된 패키지가 달라 문제가 생기면 안되기 때문이다.

```terminal
pip freeze

asgiref==3.5.2
asttokens==2.0.5
backcall==0.2.0
bcrypt==3.2.2
certifi @ file:///opt/conda/conda-bld/certifi_1655968806487/work/certifi
cffi==1.15.1
decorator==5.1.1
Django==4.0.6
django-cors-headers==3.13.0
django-extensions==3.1.5
executing==0.8.3
ipython==8.4.0
jedi==0.18.1
matplotlib-inline==0.1.3
mysqlclient==2.1.1
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.30
ptyprocess==0.7.0
pure-eval==0.2.2
pycparser==2.21
Pygments==2.12.0
PyJWT==2.4.0
six==1.16.0
sqlparse==0.4.2
stack-data==0.3.0
traitlets==5.3.0
wcwidth==0.2.5
```

`pip freeze`명령어를 입력하면 해당 가상환경에 설치된 패키지가 모두 보여진다. 여기서 본인이 직접 설치한 패키지만을 파일에 기록하도록 하자.

```txt
Django==4.0.6
django-cors-headers==3.13.0
django-extensions==3.1.5
bcrypt==3.2.2
PyJWT==2.4.0
```

## url.py 점검

프로젝트 진행 시 관리자 페이지를 별도로 사용하지 않을 것이기 때문에 admin

```python
from django.urls import path

urlpatterns = [
]
```
