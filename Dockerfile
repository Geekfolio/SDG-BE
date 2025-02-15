FROM python:3.12-slim-bookworm

WORKDIR /workspace

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["make", "start"]
