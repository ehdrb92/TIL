프록시 서버에 대한 구글의 대답은 아래와 같다.

> 프록시 서버(proxy server)는 클라이언트가 자신을 통해서 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해 주는 컴퓨터 시스템이나 응용 프로그램을 가리킨다. 서버와 클라이언트 사이에 중계기로서 대리로 통신을 수행하는 것을 가리켜 ‘프록시’, 그 중계 기능을 하는 것을 프록시 서버라고 부른다.

프록시 서버는 크게 포워드 프록시와 리버스 프록시로 나누어지게 된다.

## 포워드 프록시(Forward Proxy)

기본적으로 흔히 알고 있는 프록시를 말한다. 클라이언트 앞 단에 놓여져 있으며 클라이언트가 서버에 요청을 보내면 이를 중간에서 프록시가 가로챈다. 이후 프록시가 해당 요청을 서버에 다시 보낸다.

왜 이런 행동을 하는걸까? 정부, 학교, 기업과 같은 곳은 기관에 속한 사람들에게 제한적으로 인터넷을 사용하도록 방화벽을 사용한다. 포워드 프록시는 이러한 제한을 위해 사용한다. 해당 기관의 사람들이 특정 웹 사이트에 직접적으로 접속하는 것을 방지한다. 프록시에 접근 제한 사이트로 설정된 사이트가 있다면, 해당 기관 사람들은 접속할 수 없게 되는 것이다.

그리고 포워드 프록시는 접속자의 정보를 숨겨준다. 서버측에서 IP를 역추적해도 프록시 서버만 알 수 있게 된다.

## 리버스 프록시(Reverse Proxy)

리버스 프록시는 서버의 앞 단에 놓이게 된다. 그러면 서버는 왜 사용할까?

첫 번째로 로드밸런싱 역할을 한다. 대량의 트래픽이 발생하는 서버가 있다면 이를 모두 감당하기 힘들 수 있다. 리버스 프록시는 서버의 앞 단에서 로드밸런싱을 하며 트래픽이 서버별로 분산되도록 해준다.

두 번째로 보안을 강화한다. 포워드 프록시와 같이 서버 측의 IP를 직접적으로 드러내지 않기에 DDOS 공격을 방지할 수 있다. 하지만 CDN과 같은 리버스 프록시 서버가 타겟이 될 수는 있다.

세 번째는 캐시 데이터를 저장할 수 있다. 만약 한국의 유저가 미국의 웹 서버에 있는 데이터를 원할 때, 해당 웹 서버가 한국에 리버스 프록시 서버를 가지고 있다면 캐시 데이터를 전달하여 응답 속도를 빠르게 할 수 있다.

마지막으로 SSL 암호화에 좋다. 본래 서버가 클라이언트들과 통신을 할때 SSL(or TSL)로 암호화, 복호화를 할 경우 비용이 많이 들게 된다. 그러나 리버스 프록시를 사용하면 들어오는 요청을 모두 복호화하고 나가는 응답을 암호화해주므로 클라이언트와 안전한 통신을 할수 있으며 본래 서버의 부담을 줄여준다.