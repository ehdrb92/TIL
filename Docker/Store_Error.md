# docker.errors.DockerException: Credentials store error: StoreError

도커를 터미널에 발생한 에러

```terminal
docker.errors.DockerException: Credentials store error: StoreError('Credentials store docker-credential-desktop exited with "error getting credentials - err: exit status 1, out: `exit status 2: gpg: decryption failed: No secret key`".')
```

저장소에러....라고 하는데.... 이 에러가 발생한 원인은 무었일까??

바로 구글링해보았다. stackoverflow에 나와 비슷한 오류가 발생한 사람이 있었다.

답변내용은 아래와 같다.

It is an issue with docker build; cos, the docker hub login must fail in your case (this might have happened with multiple docker login registry in your config file)

If you want a quick fix, delete the .docker/config.json file and login docker before you run docker-compose up

Note: a new ~/.docker/config.json file will be created on your successful login

도대체가 무슨 말일까.... 당황스럽다.

일단 해결 방법은 아래와 같다.

```terminal
sudo rm ~/.docker/config.json

docker login

docker-compose up
```

일단 위의 명령어를 순서대로 실행하니 문제는 해결되었다!
