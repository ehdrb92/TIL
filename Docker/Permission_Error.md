# Permission Error

터미널에서 도커에 로그인을 하려는 데 아래와 같은 오류가 발생하였다.

```terminal
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/auth": dial unix /var/run/docker.sock: connect: permission denied
```

이유는 리눅스에서 root 권한이 아닌 상태로 도커를 실행하면 위와 같은 권한문제가 발생할 수 있다고 한다.

해결방법은 아래와 같다.

1. docker group을 생성해준다. 보통은 이미 생성되어 있다고 한다. 나는 이미 생성되어 있었음.

    `sudo groupadd docker`

2. docker group에 유저를 추가해 준다. ($USER은 유저이름을 넣어준다.)

    `sudo usermod -aG docker $USER`

3. 유더의 그룹 ID를 도커로 변경해준다.

    `newgrp docker`

일단 위의 명령대로 실행해주니 문제는 해결!
