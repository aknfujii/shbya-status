FROM node:15.5.0-alpine

WORKDIR /opt/app

COPY . /opt/app
RUN npm install

RUN npm run build

RUN npm install -g serve
CMD serve -p $PORT -s build
