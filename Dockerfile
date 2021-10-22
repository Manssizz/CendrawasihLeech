FROM breakdowns/mega-sdk-python:latest

RUN mkdir ./CendrawasihLeech
RUN chmod 777 ./CendrawasihLeech
WORKDIR /CendrawasihLeech

ENV TZ=Asia/Jakarta

RUN apt -qq update --fix-missing && \
    # apt -qq install -y git aria2 wget curl busybox ffmpeg \
    apt install jq pv openssl \
    rm -rf /var/lib/apt/lists/* && \
    apt -qq update

RUN wget https://rclone.org/install.sh
RUN bash install.sh

RUN mkdir /CendrawasihLeech/Leech
RUN wget -O /CendrawasihLeech/Leech/gclone.gz https://git.io/JJMSG
RUN gzip -d /CendrawasihLeech/Leech/gclone.gz
RUN curl -O /usr/local/bin/megadown https://raw.githubusercontent.com/masterofthesith/megadown/master/megadown
RUN chmod a+rx /usr/local/bin/megadown
RUN wget -O /usr/share/fonts/Hack-Bold.ttf file.luxing.im/dirLIST_files/download.php?file=Li9zaGFyZS9IYWNrLUJvbGQudHRm
RUN chmod 0775 /CendrawasihLeech/Leech/gclone

# RUN wget -O /CendrawasihLeech/dht.dat https://raw.githubusercontent.com/P3TERX/aria2.conf/master/dht.dat
# RUN wget -O /CendrawasihLeech/dht6.dat https://raw.githubusercontent.com/P3TERX/aria2.conf/master/dht6.dat

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
COPY extract /usr/local/bin
COPY .netrc $HOME/.netrc
RUN touch $HOME/.netrc && chmod a-rwx,u+rw $HOME/.netrc

CMD ["bash","start.sh"]
