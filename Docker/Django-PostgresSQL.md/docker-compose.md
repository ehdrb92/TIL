# Django와 PostgreSQL app setup

도커 컴포즈를 이용하여 Django/PostgreSQL app을 셋업하는 방법에 대한 정리.

이번 과정은 도커 공식문서를 참고하여 실행해 보았다.

## 프로젝트 구성요소 정의하기

1. 프로젝트 디렉토리 만들기

    내가 짓고 싶은 적절한 이름으로 프로젝트를 실행하기 위한 빈 디렉토리를 하나 만들어 준다.

    디렉토리에는 프로젝트 관련 파일 이외에 다른 파일이 포함되지 않도록 한다.

2. DockerFile 만들기

    도커 이미지 파일의 빌드를 위한 `DockerFile`을 만들어 준다.

    `DockerFile`의 내용을 현재 내가 직접 만들 수가 없어 우선은 문서상에서 제시해 주는 내용을 그대로 가져다 쓰겠다.

    ```docker
    FROM python:3
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    WORKDIR /code
    COPY requirements.txt /code/
    RUN pip install -r requirements.txt
    COPY . /code/
    ```

    위의 `Dockerfile`은 python3 버전의 이미지를 사용한다. `/code` 디렉토리에서 동작하며, `requirements.txt`파일의 패키지를 자동으로 설치한다.

3. requrements.txt 파일 작성하기

    필요한 패키지를 정리한 목록을 만들어 준다.

    ```text
    Django>=3.0,<4.0
    psycopg2>=2.8
    ```

4. docker-compose.yml 작성하기

    `docker-compose.yml`파일은 해당 프로젝트에서 웹 서버와 데이터베이스를 만드는 서비스를 실행한다. 또한 서비스에서 사용하는 도커 이미지, 연결 방법, 컨테이너 내부에 마운트해야 할 볼륨이 설명되어 있다. 마지막으로 서비스의 포트에 대해 설명되어 있다.

    ```docker
    version: "3.9"
    
    services:
    db:
        image: postgres
        volumes:
        - ./data/db:/var/lib/postgresql/data
        environment:
        - POSTGRES_DB=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
    web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
        - .:/code
        ports:
        - "8000:8000"
        environment:
        - POSTGRES_NAME=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
        depends_on:
        - db
    ```

## 장고 프로젝트 만들기

이전 과정에서 정의된 문서를 통해 장고 프로젝트를 생성하는 과정이다.

1. 프로젝트의 최상단 디렉토리로 이동한다.

2. 장고 프로젝트를 생성하기 위해 아래의 명령어를 실행한다.

    ```terminal
    sudo docker-compose run web django-admin startproject composeexample .
    ```

    이 명령어는 도커 컨테이너 안에서 `django-admin startproject composeexample`을 실행한 것과 같은 명령이다.

    웹 이미지가 아직 존재하지 않는 상황이기 때문에, `docker-compose.yml`의 `build`에 정의된대로 현재 디렉토리에 프로젝트를 만든다.

    명령어를 실행시키면 프로젝트 디렉토리에 파일들이 생성된 모습을 볼 수 있다.

    ```terminal
    drwxr-xr-x 2 root    root    4.0K  8월 19 14:40  composeexample
    drwxr-xr-x 3 root    root    4.0K  8월 19 14:40  data
    -rw-rw-r-- 1 ehdrb92 ehdrb92  496  8월 19 14:06  docker-compose.yml
    -rw-rw-r-- 1 ehdrb92 ehdrb92  159  8월 19 14:07  Dockerfile
    -rwxr-xr-x 1 root    root     670  8월 19 14:40  manage.py
    -rw-rw-r-- 1 ehdrb92 ehdrb92   30  8월 19 14:07  requirements.txt
    -rw-r--r-- 1 ehdrb92 ehdrb92 2.5K  8월 19 14:36 'ystemctl start docker'
    ```

    나의 경우에는 도커 자습서와는 다르게 `'ystemctl start docker'`라는 파일이 하나 더 생성되었다....

    이 파일은 도대체 어디서 무슨 목적으로 생성된 것일까???

    위의 파일 목록을 보면 composeexample, data, manage.py 파일에 대하여 root가 권한을 가진 모습을 볼 수 있다.

    이는 컨테이너가 루트 사용자로 실행되기 때문이라고 한다.

## 장고와 데이터베이스 연결하기

1. 프로젝트 폴더에서 `settings.py`파일을 수정해준다.

2. 아래와 같이 `os`모듈을 불러오고, `DATABASES`를 수정해준다.

    ```python
    import os
    
    [...]
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': 5432,
        }
    }
    ```

3. `docker-compose up`명령어를 프로젝트 최상위 디렉토리에서 실행시켜 준다.

    ```terminal
    Starting ikaria_db_1 ... done
    Starting ikaria_web_1 ... done
    Attaching to ikaria_db_1, ikaria_web_1
    db_1   | 
    db_1   | PostgreSQL Database directory appears to contain a database; Skipping initialization
    db_1   | 
    db_1   | 2022-08-19 06:30:37.602 UTC [1] LOG:  starting PostgreSQL 14.5 (Debian 14.5-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
    db_1   | 2022-08-19 06:30:37.602 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
    db_1   | 2022-08-19 06:30:37.602 UTC [1] LOG:  listening on IPv6 address "::", port 5432
    db_1   | 2022-08-19 06:30:37.604 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    db_1   | 2022-08-19 06:30:37.608 UTC [27] LOG:  database system was shut down at 2022-08-19 06:30:33 UTC
    db_1   | 2022-08-19 06:30:37.611 UTC [1] LOG:  database system is ready to accept connections
    web_1  | Watching for file changes with StatReloader
    web_1  | Performing system checks...
    web_1  | 
    web_1  | System check identified no issues (0 silenced).
    web_1  | 
    web_1  | You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    web_1  | Run 'python manage.py migrate' to apply them.
    web_1  | August 19, 2022 - 06:30:38
    web_1  | Django version 3.2.15, using settings 'composeexample.settings'
    web_1  | Starting development server at http://0.0.0.0:8000/
    web_1  | Quit the server with CONTROL-C.
    web_1  | [19/Aug/2022 06:30:52] "GET / HTTP/1.1" 200 10697
    web_1  | [19/Aug/2022 06:30:52] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
    web_1  | [19/Aug/2022 06:30:53] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
    web_1  | [19/Aug/2022 06:30:53] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
    web_1  | [19/Aug/2022 06:30:53] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
    web_1  | Not Found: /favicon.ico
    web_1  | [19/Aug/2022 06:30:53] "GET /favicon.ico HTTP/1.1" 404 2118
    ^CGracefully stopping... (press Ctrl+C again to force)
    Stopping ikaria_web_1 ... done
    Stopping ikaria_db_1  ... done

    ```

    실행되면 장고 어플리케이션이 도커 호스트의 8000번 포트에서 실행된다.

    그리고 `http://localhost:8000`로 접속하면 장고 서버에 정확히 접속이 되는 모습을 확인할 수 있다.

4. `docker ps`명령어로 가동 중인 컨테이너를 확인할 수 있다.

    ```terminal
    CONTAINER ID   IMAGE        COMMAND                  CREATED          STATUS              PORTS                                       NAMES
    625807ce8aa8   ikaria_web   "python manage.py ru…"   33 minutes ago   Up About a minute   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   ikaria_web_1
    9b2d8401313c   postgres     "docker-entrypoint.s…"   52 minutes ago   Up About a minute   5432/tcp                                    ikaria_db_1
    ```

5. 서버를 종료하려면 `docker-compose down`또는 `Ctrl + C`를 하여 종료시킬 수 있다.