# SSAFY_Daliy_Project

## 200311|Day03| 도커 실습

### 도커

-  프로세스 격리에 기반한 가상화 방법 중 하나가 컨테이너형 가상화 기술
- 단순히 가상 머신의 역할을 넘어서 어느 플랫폼에서나 이전의 상태를 그대로 재현가능한 애플리케이션 컨테이너를 운용하는 것을 목표
- 리눅스에서 제공하는 컨테이너를 이용하여 애플리케이션을 묶어서 실행, 배포 할 수 있게 해주는 오픈 소스 SW



### 산출물

#### front-end

- skeleton code 다운로드



-  로컬에서 프론트 실행 및 웹 브라우져로 접속(http://[Docker IP 주소]:8080)해서 확인

```
cd front-sk
yarn install
yarn serve
```



- front-sk 폴더 안에 Dockerfile 생성 

```
FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
```

- 빌드

```
docker build . -t front:0.1
```



- 이미지에 TAG 추가하기

```
$ docker tag front:0.1 front:latest
```



- 이미지에 TAG 삭제하기

```
$ docker rmi front
Untagged: front:latest
```



- 도커로 프론트 실행 및 웹 브라우져로 접속

```
$ docker run -it -p 80:8080 --rm front:0.1
```



#### back-end

- 로컬에서 백엔드 실행

```
$ cd back-sk
$ mvnw package
$ java -jar target/webcuration-0.0.1-SNAPSHOT.jar
```

```
$ sudo ./mvnw package
```

- back-sk 폴더 안에 Dockerfile 생성

```
$docker build . -t back:0.1
...
Successfully built 71d57b43c6ec
Successfully tagged back:0.1

$ docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
back 0.1 71d57b43c6ec 39 hours ago 134MB
front 0.1 b35805335785 39 hours ago 22.7MB

```

- 도커로 백엔드 실행

```
docker run -it -p 8080:8080 --rm back:0.1
```