FROM python:3.7-slim-buster

RUN apt-get update
RUN apt-get -y install gcc libgl1-mesa-dev libglib2.0-0
ENV TZ=Asia/Tokyo

WORKDIR /opt/app

COPY requirements.txt /opt/app
RUN pip install -r requirements.txt

COPY . /opt/app
RUN python testdata/download_models.py

RUN python manage.py init_db


