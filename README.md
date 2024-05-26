# Minecraft Docker

Run minecraft in docker.
Supports openjdk11, 17 and 21.
can be build for amd64 and arm64.

## Using

```docker run -v minecraft:/server -p 25565:25565 strixvyxlor/minecraft-docker:master-jdk21```

**note
this container will crash when useing jdk11 or jdk17.
this is not an error, the preinstalled fabric server is 1.20.6 and thus will crash with these versions.

## Building

run the build.py script.
args explaind by script.
