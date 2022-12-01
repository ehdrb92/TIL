Django를 이용해 프로젝트를 진행하며 "python manage.py runserver"라는 명령어를 많이 써왔다. 나는 이 명령어가 사실상 서버 컴퓨터에서 배포를 하는 것과 같은 의미라고 생각해왔다. 그런데 실제로 배포를 하는 과정을 인터넷에서 찾아보면 Apache, Nginx와 같은 웹 서버를 함께 사용한다고 나온다. 왜 굳이 이러한 웹 서버를 별도로 사용해야 할까에 대한 의문점이 생겼다.

Django의 공식 문서상에 runserver와 관련된 내용을 보면 아래와 같은 경고문구가 있다.

> DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests. (And that’s how it’s gonna stay. We’re in the business of making Web frameworks, not Web servers, so improving this server to be able to handle a production environment is outside the scope of Django.)

해석해보면, 운영 환경에서 이 서버를 사용하지 마십시오. 보안 감사나 성능 테스트를 거치지 않았습니다. (우리는 웹 서버가 아닌 웹 프레임워크를 만드는 사업을 하고 있기 때문에 이 서버를 개선하여 운영 환경을 처리하는 것은 장고의 범위 밖입니다.)

결론은 실제 운영 환경에서 쓰기에는 성능하고 보안이 좋지 않다는 말이다.(테스트 및 디버깅 용)

그러니 실제로 배포 및 운영을 하려고 하면 별도의 Nginx, Gunicorn과 같은 WS, WSGI 등을 함께 사용해야 한다.