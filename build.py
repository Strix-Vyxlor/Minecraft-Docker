#!/usr/bin/python3

import sys
import os
import subprocess

argc = len(sys.argv)

if argc != 3:
    print("not enough arguments --> python build.py $JDK_VERSION $ARCH")
    exit()

jdk = None
arch = None

if sys.argv[1] not in ["21", "17", "11"]:
    print("jdk versions: 21, 17, 11")
    exit()
jdk = sys.argv[1]

if sys.argv[2] not in ["arm64", "amd64"]:
    print("supported arch: arm64/v8, amd64")
    exit()

arch = sys.argv[2]

subprocess.run(["docker", "buildx", "build",
            "--tag", f"minecraft-docker:latest-jdk{jdk}-{arch}",
            "--target", f"latest-jdk{jdk}",
            "--platform", f"linux/{arch}",
            "--builder", "minecraft",
            "--load", "."])

