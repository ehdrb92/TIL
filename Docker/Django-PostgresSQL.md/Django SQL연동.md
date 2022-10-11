# PostgresSQL 데이터베이스 생성

먼저 postgresSQL의 컨테이너 내부 Shell로 진입해준다.

`docker exec -it {컨테이너ID 또는 이름} /bin/bash`

쉘로 진입 후 postgres에 접속하여 만들어준 사용할 유저와 데이터베이스를 만들어 준다.

그리고 postgres의 쉘로 접근한다.

유저와 데이터베이스를 생성하지 않은 경우 생성하여 준다.

* postgresSQL 명령어

유저 생성 명령어

`create user {유저명} password {패스워드} superuser`

데이터베이스 생성 명령어

`create database {데이터베이스명} owner {유저명}`

데이터베이스 접속 명령어

`psql -U {유저명} {데이터베이스명}`

그리고 `docker-compose.yml`파일을 수정한다.

```docker
version: "3.9"
   
services:
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=ikaria # 기존에는 postgres
      - POSTGRES_USER=donggyu # 기존에는 postgres
      - POSTGRES_PASSWORD=donggyu # 기존에는 postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_DB=ikaria # 기존에는 postgres
      - POSTGRES_USER=donggyu # 기존에는 postgres
      - POSTGRES_PASSWORD=donggyu # 기존에는 postgres
    depends_on:
      - db
```

이후 프로젝트 폴더에서 `users`앱을 생성시켜 주었다.

`python manage.py startapp users`

앱을 생성시켜 주고, 유저의 ip정보를 담을 테이블 모델을 생성시키기 위해 models.py에 데이터를 추가하였다.

```python
from django.db import models

class User(models.Model):
    user_ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
```

그리고 makemigration과 migrate를 통하여 데이터베이스에 테이블을 생성하였다.

```terminal
python manage.py makemigrations
python manage.py migrate
```
