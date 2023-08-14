# API 관련 사항

## requirements

python 3.10.6

```console
pip install -r requirements.txt
```

## api local

```console
sh run-api.sh
```

```console
sh stop-api.sh
```

## 배포

1. 먼저 프로젝트 루트 디렉토리에 .env파일을 생성하고 전달 받은 .env 키, 값을 넣어주세요

2. firebase-service-key.json 파일을 루트 디렉토리에 넣어줍니다.

3. 콘솔에 아래와 같이 입력하세요

```console
sh deploy.sh
```

```console
sh destroy.sh
```

## 도커 용량 비우기

```console
sudo docker system prune
sudo docker volume prune -a
sudo docker image prune -a
```

## docker 없이 실행

```console
sudo cp api.service /etc/systemd/system/api.service
sudo systemctl daemon-reload
sudo systemctl start api.service

# restart
sudo systemctl restart api.service

# status
sudo systemctl status api.service
```

* log 조회

```console
journalctl -u api.service
```
