FROM jenkins/jenkins:lts

# Install python:
USER root
RUN apt-get update && apt-get install -y python3 python3-pip
USER jenkins