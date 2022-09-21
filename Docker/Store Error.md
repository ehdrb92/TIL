# docker.errors.DockerException: Credentials store error: StoreError

도커를 터미널에 발생한 에러

```terminal
docker.errors.DockerException: Credentials store error: StoreError('Credentials store docker-credential-desktop exited with "error getting credentials - err: exit status 1, out: `exit status 2: gpg: decryption failed: No secret key`".')
```

같은 오류상황에서 stackoverflow 답변내용은 아래와 같다.

It is an issue with docker build; cos, the docker hub login must fail in your case (this might have happened with multiple docker login registry in your config file)

If you want a quick fix, delete the .docker/config.json file and login docker before you run docker-compose up

Note: a new ~/.docker/config.json file will be created on your successful login

일단 해결 방법은 아래와 같다.

```terminal
sudo rm ~/.docker/config.json

docker login

docker-compose up
```

일단 위의 명령어를 순서대로 실행하니 문제는 해결되었다!
