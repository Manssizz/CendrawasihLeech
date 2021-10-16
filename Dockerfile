# FROM breakdowns/mega-sdk-python:latest
FROM ubuntu:20.04

RUN mkdir ./CendrawasihLeech
RUN chmod 777 ./CendrawasihLeech
WORKDIR /CendrawasihLeech

ENV TZ=Asia/Jakarta

RUN apt-get -qq update && \
	    DEBIAN_FRONTEND="noninteractive" apt-get -qq install -y wget tzdata aria2 git python3 python3-pip \
	    locales python3-lxml \
	    curl pv jq ffmpeg \
	    p7zip-full p7zip-rar \
	    libcrypto++-dev libssl-dev \
	    libc-ares-dev libcurl4-openssl-dev \
	    libsqlite3-dev libsodium-dev && \
	    curl -L https://github.com/jaskaranSM/megasdkrest/releases/download/v0.1/megasdkrest -o /usr/local/bin/megasdkrest && \
	    chmod +x /usr/local/bin/megasdkrest

# RUN apt -qq update --fix-missing && \
#     rm -rf /var/lib/apt/lists/* && \
#     apt -qq update
#     apt -qq install -y git aria2 wget curl busybox ffmpeg

RUN wget https://rclone.org/install.sh
RUN bash install.sh

RUN mkdir /CendrawasihLeech/Leech
RUN wget -O /CendrawasihLeech/Leech/gclone.gz https://git.io/JJMSG
RUN gzip -d /CendrawasihLeech/Leech/gclone.gz
RUN chmod 0775 /CendrawasihLeech/Leech/gclone

# RUN wget -O /CendrawasihLeech/dht.dat https://raw.githubusercontent.com/P3TERX/aria2.conf/master/dht.dat
# RUN wget -O /CendrawasihLeech/dht6.dat https://raw.githubusercontent.com/P3TERX/aria2.conf/master/dht6.dat

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
COPY extract /usr/local/bin
COPY .netrc $HOME/.netrc
# RUN chmod +x /usr/local/bin/extract && chmod 600 /root/.netrc
RUN touch $HOME/.netrc && chmod a-rwx,u+rw $HOME/.netrc

CMD ["bash","start.sh"]
