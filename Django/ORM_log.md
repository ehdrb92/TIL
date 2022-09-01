# 장고 ORM 기록조회

우리가 데이터베이스의 데이터를 조작 및 조회할 때 MySQL 명령문을 사용하지 않고 파이썬 언어를 이용한 ORM(Object Relational Mapping)을 통해 간단하게 데이터 조작이 가능하다.

그런데 여기서 ORM이 어떤식으로 데이터 정보에 접근하고 조작하는지 궁금할 수 있다. 이때 이 기록들을 조회하는 방법이 있다고 한다.

```python
#settings.py
LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

위와 같이 코드를 settings.py에 작성하면 서버가 가동중인 화면 또는 쉘에서 데이터에 접근할 때 해당 로그가 반환된다.

![logging(1)](./image/logging(1).png)

![logging(2)](./image/logging(2).png)

또는 따로 파일로 저장하여 기록을 남기고 싶다면 아래와 같이 코드를 작성해 줄 수 있다.

```python
#settings.py

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
         'verbose': {
            'format': '{asctime} {levelname} {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'class'     : 'logging.StreamHandler',
            'formatter' : 'verbose',
            'level'     : 'DEBUG',
        },
        'file': {
            'level'     : 'DEBUG',
            'class'     : 'logging.FileHandler',
            'formatter' : 'verbose',
            'filename'  : 'debug.log',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers' : ['console','file'],
            'level'    : 'DEBUG',
            'propagate': False,
        },
    },
}
```

![logging(3)](./image/logging(3).png)
