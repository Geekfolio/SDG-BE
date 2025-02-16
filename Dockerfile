FROM python:3.12-slim-bookworm

WORKDIR /workspace

RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN make init db

EXPOSE 8080

ENTRYPOINT ["make", "start"]
