# Docker 기본 작동

```terminal
docker run -d -p 80:80 docker/getting-started
# == docker run -dp 80:80 docker/getting-started 
```

이미지를 컨테이너를 통해 가동시키는 명령어이다.

명령어의 의미는 아래와 같다.

- `-d` : 컨테이너를 분리 모드(백그라운드에서)로 실행한다.
- `-p 80:80` : 호스트의 80번 포트를 컨테이너의 80번 포트에 매핑한다. `http://localhost:80`로 접근할 수 있다.
호스트의 80번 포트가 수신하는 서비스가 이미 존재할 경우 다른 포트를 지정해야 한다.
예를 들어 `-p 3000:80`은 호스트의 3000번 포트에 매핑하여 `http://localhost:3000`로 접근할 수 있다.
- `docker/getting-started` : 사용할 이미지를 지정한다.

이미지를 만들기 위해서는 `Dockerfile`을 작성해야 한다.

```docker
# Dockerfile
# syntax=docker/dockerfile:1
FROM node:12-alpine
RUN apk add --no-cache python2 g++ make
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
```

Dockerfile이 존재하는 경로로 이동하여 아래의 명령어를 입력하면 이미지를 생성할 수 있다.

```terminal
# 이미지 생성 명령어
# '.'은 Dockerfile이 현재 디렉토리에 위치함을 말한다.
docker build -t getting-started .
```

실행 중인 컨테이너 관련 명령어

```terminal
docker ps # 현재 실행 중인 컨테이너 목록
docker stop <the-container-id> # 컨테이너 실행 중지 명령
docker rm <the-container-id> # 컨테이너 삭제 명령
docker rm -f <the-container-id> # 컨테이너 강제 삭제 명령
```

이미지 공유 관련 명령어

```terminal
docker tag <기존 이미지명> <username>/<수정할 이미지명>:<태그명> # 같은 이미지를 다른 이름으로 복사하는 명령어
docker push <username>/<이미지명>:<태그명> # 허브에 push 명령, 태그명을 생략할 경우 기본값인 'latest'가 붙는다.
```

