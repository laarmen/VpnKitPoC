FROM alpine:latest
ADD . /code
WORKDIR /code
RUN apk update
RUN apk add python py-curl
CMD ["python", "app.py"]
