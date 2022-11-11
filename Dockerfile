FROM python:3-alpine
WORKDIR /app
COPY . /app/
RUN apk add --no-cache bash && \
    apk --update add python3 curl && \ 
    pip3 install -r requirements.txt