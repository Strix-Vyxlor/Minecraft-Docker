FROM alpine:latest as latest-jdk21

RUN apk update
RUN apk upgrade

COPY server /server
RUN apk add openjdk21-jre

EXPOSE 25565

WORKDIR /server
ENTRYPOINT ash ./run.sh

FROM alpine:latest as latest-jdk17

RUN apk update
RUN apk upgrade

COPY server /server
RUN apk add openjdk17-jre

EXPOSE 25565

WORKDIR /server
ENTRYPOINT ash ./run.sh

FROM alpine:latest as latest-jdk11

RUN apk update
RUN apk upgrade

COPY server /server
RUN apk add openjdk11-jre

EXPOSE 25565

WORKDIR /server
ENTRYPOINT ash ./run.sh

