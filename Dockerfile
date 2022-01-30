# syntax=docker/dockerfile:1
FROM frolvlad/alpine-python2
WORKDIR /radioshark
COPY . .
RUN apk add python2-dev musl-dev eudev-dev linux-headers gcc libusb-dev hidapi git
RUN git clone https://github.com/awelkie/pyhidapi.git; cd pyhidapi; python setup.py install; cd -
