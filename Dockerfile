FROM python:3.10.6-slim

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    openssl libssl-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 7860

ENTRYPOINT ["sh", "entrypoint.sh"]
