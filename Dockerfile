FROM ubuntu:20.04
# FROM lzzy12/mega-sdk-python:latest

# WORKDIR /usr/src/app
# RUN chmod 777 /usr/src/app
RUN mkdir ./CendrawasihLeech
RUN chmod 777 ./CendrawasihLeech
WORKDIR /CendrawasihLeech

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Jakarta

RUN apt -qq update --fix-missing && \
    apt -qq install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/* && \
    # apt add-repository non-free && \
    apt-add-repository 'https://packages.medibuntu.org free non-free' \
    apt -qq update && \
    apt -qq install -y git aria2 wget curl busybox unzip \
    python3 ffmpeg python3-pip p7zip-full p7zip-rar \
    locales \
    apt purge -y software-properties-common    

RUN wget https://rclone.org/install.sh
RUN bash install.sh

RUN mkdir /CendrawasihLeech/Leech
RUN wget -O /CendrawasihLeech/Leech/gclone.gz https://git.io/JJMSG
RUN gzip -d /CendrawasihLeech/Leech/gclone.gz
RUN chmod 0775 /CendrawasihLeech/Leech/gclone

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY extract /usr/local/bin
RUN chmod +x /usr/local/bin/extract
COPY .netrc /root/.netrc
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
COPY . .

CMD ["bash","start.sh"]
