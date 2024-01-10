FROM ubuntu:latest
LABEL authors="jchestnut"

ENTRYPOINT ["top", "-b"]