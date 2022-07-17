# HTTP

HTTP는 `HyperText Transfer Protocol`의 약자이다. 뜻하는 바가 무엇인지, 그리고 HTTP의 특징에 대해 알아보았다.

## HyperTxet

HTML에서의 의미와 동일하다. 문서와 문서가 링크로 연결되도록 하는 태그로 구성된 언어라는 뜻이다.

## Transfer

해석그대로 "전송하다"라는 의미를 가진다. 우리가 HTML 등의 언어로 작성된 페이지를 다른 특정 대상에게 전달한다는 의미이다.
전송은 보내는 주체와 받는 주체가 존재한다.

## Protocol

프로토콜은 협약, 통신 규약이라는 의미를 가진다. 물리적으로 떨어진 컴퓨터 끼리 어떻게 HTML파일을 주고 받을 지에 대한 약속이다. 인터넷에서 어떤 요청을 하고 이에 대한 응답을 주는데 어떤식으로 소통할 것인지에 대한 약속이다.

**결론적으로 HTTP란 컴퓨터들이 HTML파일을 주고받을 수 있도록 하는 소통방식 또는 약속이다.**

## Request/Response (요청/응답)

HTTP 통신의 핵심은 요청과 응답이다. 약속된 요청을 잘 보내고 응답을 잘 받는게 중요하다.
컴퓨터가 인터넷에서 요청을 하고 응답을 받는 과정을 살펴보자.

### Request 메세지 구조

HTTP의 요청은 프론트엔드(클라이언트)에서 백엔드(서버)에 데이터 처리를 시작하게 하는 메세지이다. 이 메세지는 크게 세 부분으로 나뉜다.

* Start Line

HTTP Method : 해당 요청이 의도한 액션을 정의하는 부분  
Request target : 해당 request가 전송되는 목표 url  
HTTP Version : 사용되는 HTTP 버전

* Headers

해당 요청에 대한 추가 정보(메타 데이터)를 담고있는 부분이다.

Key : Value 값으로 되어있다 (JavaScript의 객체, Python의 딕셔너리 형태라고 보면 된다)  
Host : 요청을 보내는 목표(타겟)의 주소. 즉, 요청을 보내는 웹사이트의 기본 주소가 된다. (ex. www.apple.co.kr)  
User-Agent : 요청을 보내는 클라이언트의 대한 정보 (ex. chrome, firefox, safari)  
Content-Type : 해당 요청이 보내는 메세지 body의 타입 (ex. application/json)  
Content-Length : body 내용의 길이  
Authorization : 회원의 인증/인가를 처리하기 위해 로그인 토큰을 Authroization 에 담는다

```terminal
Headers: {
    Host:  
    User-Agent:
    Content-Type:
    Content-Length:
    Authorization:
}
```

* Body

해당 요청의 실제 내용이 포함되는 곳이다.

ex) 로그인 시에 서버에 보낼 내용

```terminal
"user_email":"wecode@gmail.com" "user_password": "wecode"
```

### Response 메시지 구조

HTTP 응답 구조 또한 세 부분으로 나뉜다.

* Status Line

HTTP Version : 사용되는 HTTP 버전  
Status Code: 응답 메세지의 상태 코드  
Status Text: 응답 메세지의 상태를 간략하게 설명해주는 텍스트

```terminal
HTTP/1.1 404 Not Found
# 해석: HTTP 1.1 버전으로 응답하고 있는데, 프론트엔드에서 보낸 요청(ex. 로그인 시도)에 대해서
# 유저의 정보를 찾을 수 없기 때문에(Not Found) 404 상태 메세지를 보낸다.

HTTP/1.1 200 SUCCESS
# 해석: HTTP 1.1 버전으로 응답하고 있는데, 프론트엔드에서 보낸 요청에 대해서 성공했기 때문에
# 200 상태 메세지를 보낸다.
```

* Header

응답에서만 사용되는 헤더의 정보들이 있습니다. (ex. 요청하는 브라우저의 정보가 담긴 User-Agent 대신, Server 헤더가 사용됩니다.)

* Body

요청의 메소드에 따라 Body가 항상 존재하지 않듯이 응답도 응답의 형태에 따라 데이터를 전송할 필요가 없는 경우엔 Body가 없을 수도 있습니다.</br>
가장 많이 사용되는 Body 의 데이터 타입은 JSON(JavaScript Object Notation) 입니다.</br>
로그인 요청에 대해 성공했을 때 응답의 내용

```terminal
Body: {
    "message": "SUCCESS"
    "token": "kldiduajsadm@9df0asmzm" (암호화된 유저의 정보)
}
```
