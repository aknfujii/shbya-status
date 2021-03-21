FROM python:3.9.1

RUN apt-get update
RUN apt-get -y install gcc libgl1-mesa-dev wget
ENV TZ=Asia/Tokyo
#RUN apk --update add tzdata && \
#    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
#    apk del tzdata && \
#    rm -rf /var/cache/apk/*

COPY . /opt/app

WORKDIR /opt/app
RUN pip install -r requirements.txt
WORKDIR /opt/app/testdata
RUN python download_models.py
RUN wget --no-check-certificate https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/ssd_mobilenet_v2_coco_2018_03_29.pbtxt
WORKDIR /opt/app

RUN pip install -r requirements.txt
RUN python manage.py init_db

ENV GOOGLE_APPLICATION_CREDENTIALS=certificate.json
ENV FLASK_APP /opt/app/server.py
CMD gunicorn server:app -b 0.0.0.0:$PORT --log-file -
#ENTRYPOINT flask run -h 0.0.0.0 -p $PORT

