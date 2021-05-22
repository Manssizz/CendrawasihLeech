FROM ubuntu:20.04

RUN mkdir ./app
RUN chmod 777 ./app
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Jakarta

RUN apt -qq update --fix-missing && \
    apt -qq install -y git p7zip-full p7zip-rar aria2 curl \
    ffmpeg python3 python3-pip wget busybox
    
RUN wget https://rclone.org/install.sh
RUN bash install.sh

RUN mkdir /app/manssizz
RUN wget -O /app/manssizz/gclone.gz https://git.io/JJMSG
RUN gzip -d /app/manssizz/gclone.gz
RUN chmod 0775 /app/manssizz/gclone

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US:en
# ENV LC_ALL en_US.UTF-8
COPY . .
COPY .netrc /root/.netrc
RUN chmod +x tracker.sh
RUN chmod +x rclone.sh
CMD ["bash","start.sh"]
