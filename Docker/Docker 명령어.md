# Docker 명령어 정리

```terminal

# 도커 버전확인
docker -v

# 도커 이미지 받기
# 모든 명령에서 태그의 경우 필수사항은 아니다.
docker pull {이미지명}:{태그}
# 예: docker pull python:3

# 도커 이미지 목록
docker images

# 도커 컨테이너 생성
docker create {옵션} {이미지명}:{태그}
# 예: docker create -it python

# 컨테이너 시작하기
docker start {컨테이너 id 또는 이름}

# 컨테이너 내 CLI 이용하기
docker attach {컨테이너 id 또는 이름}

# 이미지로 컨테이너 만들어 시작하기
docker run {이미지명}:{태그}
# 예: docker -it run python:3
```

## 옵션정리

| Option                                     | Description                                                       |
|--------------------------------------------|-------------------------------------------------------------------|
| -d                                         | 데몬으로 실행(백그라운드 실행)                                          |
| -it                                        | 컨테이너로 들어갔을 때 bash로 CLI 입출력을 사용할 수 있게 해준다.            |
| --name {이름}                               | 컨테이너 이름 지정                                                   |
| -p {호스트의 포트 번호}:{컨테이너의 포트 번호}     | 호스트와 컨테이너 포트 연결                                            |
| --rm                                       | 컨테이너가 종료되면(내부 작업이 끝나면) 컨테이너가 삭제된다.                  |
| -v {호스트의 디렉토리}:{컨테이너의 디렉토리}       | 호스트와 컨테이너의 디렉토리 연결                                        |

```terminal

# 컨테이너 재시작
docker restart {컨테이너 id 또는 이름}

# 컨테이너 내부 쉘에서 빠져나오기 (컨테이너 종료)
exit 또는 Ctrl + D

# 컨테이너 내부 쉘에서 빠져나오기 (컨테이너를 종료하지 않음)
Ctrl + P, Q

# 동작 중인 컨테이너 조회
# 동작하지 않는 컨테이너까지 조회하려면 뒤에 -a 옵션 추가
docker ps

# 컨테이너 삭제
docker rm {컨테이너 id 또는 이름}

# 모든 컨테이너 삭제
docker rm `docker ps -a -q`

# 이미지 삭제
docker rmi {옵션} {이미지 id}

# 모든 컨테이너 중지
docker stop $(docker ps -aq)

# 사용되지 않는 모든 도커 요소(컨테이너, 이미지, 네트워크, 볼륨 등) 삭제
docker system prune -a

# 도커 파일로 이미지 생성
# Dockerfile 파일이 있는 디렉토리 기준.  마지막의 . 이 상대주소
docker build -t {이미지명} .

# 도커 컴포즈 실행
# docker-compose 파일이 있는 디렉토리 기준
# 백그라운드에서 데몬으로 돌도록 하려면 -d 옵션을 붙입니다.
docker-compose up
```
