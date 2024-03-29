## WS(Web Server)

- 클라이언트로부터 요청받은 리소스를 응답하는 하드웨어 또는 소프트웨어를 말한다.
- 정적 데이터를 제공한다.
- 리버스 프록시로서 역할을 한다.
- 대표적으로 Apache, Nginx가 있다.

## CGI

- 웹 서버와 외부 어플리케이션(python, javascript 등)을 연결하는 표준화된 프로토콜이다.
- 클라이언트 요청이 발생할 때마다 프로세스를 생성하고, 마치면 삭제한다.
- 위의 과정 때문에 오버헤드가 심해 성능 저하의 원인이 된다.
- FastCGI는 프로세스를 하나만 실행시켜 작업을 처리하여 CGI의 단점은 개선한 것이다.

## WSGI(Web Server Gateway Interface)

- Web Server Gateway Interface로 파이썬을 WS와 통신하게 해주는 인터페이스. 웹서버가 파이썬 언어를 읽을 수 없으니 중간의 미들웨어에 해당하는 WSGI가 대신 읽어서 결과를 반환한다.
- 한 프로세스에서 모든 요청을 받는다.
- Python WSGI 가 Ruby 에선 Rack, Java 에서는 Servlet

## WAS(Web Application Server)

- WS + CGI와 같은 개념으로 볼 수 있으며, 동적 데이터를 제공한다.
- 일반적으로 WS의 기능을 같이 가지고 있어, WAS가 있으면 별도로 WS를 사용하지 않아도 된다.

## 전체적인 흐름(WS <=> WSGI)

1. WS가 Client로 부터 HTTP Request를 받음.
2. 정적 파일이면 직접 HTTP Response
3. 아닐경우 WSGI 에게 전달.
4. WSGI는 해당 요청을 WAS 에게 전달(Callable Object)
5. WAS는 해결한 뒤 WS에게 전달.

## WS와 WAS를 같이 사용한다면 이유는 무엇일까?

목적에 따라 정적/동적인 데이터를 WS/WAS가 분산하여 처리하게 하여 한쪽에 과도한 부하를 방지하기 위해서라고 생각할 수 있지만 이는 WAS가 발전하면서 정적/동적 데이터를 함께 처리하는데 문제가 없어졌다. 오히려 WAS의 앞 단에 WS를 두는 것이 불필요한 관리 부담과 과부하를 일으킬 수 있다고 한다.

그렇다면 진짜 이유는 무엇이 있을까? 아래와 같다고 한다.

1. 하나의 웹에서 다른 언어의 어플리케이션을 운영해야 할때
2. 로드밸런싱이 필요한 경우
3. 보안적인 측면에서 강화해야 할 경우