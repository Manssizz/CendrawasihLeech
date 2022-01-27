<h1 align="center">
  <a href="https://github.com/Manssizz/CendrawasihLeech"><img src="https://i.imgur.com/CdNhEj3.png" alt="LOGO"></a>
</h1>

## About Repo
This repo based [GautamKumar](https://github.com/gautamajay52/TorrentLeech-Gdrive) TorrentLeech with some tweaks

### Tweaks
- Support thumbnail AVI, MOV, 3GP, etc. even you must download the file first
- Add aria2 advance configuration
- Support hxfile, anonfiles, letsupload, etc. based [zevtyardt](https://github.com/zevtyardt/lk21) module
- Simply status messages
- Support download private file. [Read this!](https://github.com/Manssizz/CendrawasihLeech/#netrc) 

### Branch
- Master branch is development version
- Stable branch is stable version

### Direct Links Supports
```
zippyshare.com, yadi.sk, mediafire.com, osdn.net, uservideo.xyz,
github.com, racaty.net, letsupload.io, hxfile.co, anonfiles.com,
bayfiles.com, antfiles.com, streamtape.com, 1drv.ms aka OneDrive,
mxplayer.in, pixledrain.com, solidfiles.com, pixeldrain.com,
files.im, reupload.org, mirrored.to

- Fembed with mirror domain
naniplay.nanime.in, naniplay.nanime.biz, naniplay.com, femax20.com,
feurl.com, fcdn.stream, layarkacaxxi.icu

- StreamSB with mirror domain
sbembed.com, sbembed1.com, sbembed2.com, sbembed3.com, sbembed4.com
sbplay.org, sbplay.one, streamsb.net, sbcloud1.com
```
**REMOVED**
~~cloud.mail.ru~~
> Note: if you want to mirroring fembed links, use must add https:// in front of links. ex: /mirror https://fembed.com/f/jgndzfdj-n7zyg5
### Torrent search supports list (Under development)
```
nyaa.si, sukebei, 1337x, piratebay,
tgx, yts, eztv, torlock, rarbg
```
### Thumbnail supports
```
"MKV", "MP4", "WEBM", "AVI", "MOV", 
"MPEG", "WMV", "M4V", "3GP"
```
> Note: Even stream format is support thumbnail, but telegram only support mp4 and mkv thumbnail for stream directly in app. You can still see thumbnail, but you must download the media file when you want to watch or open it.
### .netrc
.netrc used by aria or ytdl for downloading private file with login required. so... you can fill your login data into .netrc file. 
```
machine <site> login <mail/username> password <password>
i.e: 
machine vk login tai@babi.com password tai@kuda
machine facebook login tai@babi.com password tai@kuda
```
For Index Link with only password without username, even http auth will not work, so this is the solution.
```
machine taikuda.workers.dev <password> index_password
```
> `Important:` **Because personal data login is a very confidential thing, i exclude my .netrc file in gitignore. if you want add, remove netrc in gitignore and  make you repo private before you push .netrc file** 
### Sample of rClone config
<h1 align="center">
  <a href="https://github.com/Manssizz/CendrawasihLeech"><img src="https://raw.githubusercontent.com/Manssizz/CendrawasihLeech/master/rclone.jpg" alt="rClone config"></a>
</h1>

### Command List
```
leech - Leech and upload to Telegram.
clone - Clone Drive file or folder.
sync - Leech torrent/direct link to Drive.
tgsync - Mirror telegram files to ur Drive.
log - Check logs.
status - Get download/upload process status. 
stop - Stop single process command 
archive - Leech and upload as archive file on Telegram.
tarsync - Compress folder/file and upload to Drive.
extract - Extract file and upload to telegram.
untarsync - Extract file and upload to Drive.
tguntar - Extract telegram file and upload to cloud.
ytdl - Download Youtube video and upload to Telegram.
ytdlsync - Download Youtube video and upload to Drive.
getsize - Get size folder in Drive.
renewme - Cancel all download process.
pytleech - Youtube playlist downloader and send to telegram.
pytdlsync - Youtube playlist downloader and send to Drive.
upload - Hmmm... wait
tshelp - Torrent search helper.
speedtest - Check server connection speed.
rclone - [Admin Only] Change or edit rClone config.
rename - To rename the telegram files.
```

### Archive supports
```
ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2, 
APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT, 
HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, 
NTFS, RPM, SquashFS, UDF, VHD, XAR, TAR.XZ, Z.
```

### Deploy
#### VPS
- Install docker and docker.io

`# apt update && apt install docker docker.io`
- Clone stable repository

`# git clone -b stable https://github.com/Manssizz/CendrawasihLeech.git`
- Copy config file

`# cp CendrawasihLeech/sample_config.env CendrawasihLeech/config.env`
- Fill config with your data

`# nano CendrawasihLeech/config.env`
- Fill rclone.conf with your rclone data

`# nano CendrawasihLeech/rclone.conf`
- Fill .netrc with your credentials data

`# nano CendrawasihLeech/.netrc`
- Build image with this command

`# docker build -t manssizz/cendrwasihleech CendrawasihLeech/`
- Show image build for grab id image

`# docker image ls`
<h1 align="center">
  <a href="https://github.com/Manssizz/CendrawasihLeech"><img src="https://i.imgur.com/GNrYo76.png" alt="image list"></a>
</h1>

- Run docker image

`# docker run -d --rm --name CendrawasihLeech <image-id>`

- Check docker container process 

`# docker ps | grep cendrwasihleech`
<h1 align="center">
  <a href="https://github.com/Manssizz/CendrawasihLeech"><img src="https://i.imgur.com/SdcvUFO.png" alt="container list"></a>
</h1>

- Check logs bot

`# docker logs <container-id>`

#### Heroku (DEAD)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Manssizz/CendrawasihLeech/tree/stable)

### Credits
* [GautamKumar](https://github.com/gautamajay52/TorrentLeech-Gdrive) for original source.
* [SlamMirror](https://github.com/breakdowns/slam-mirrorbot) I pick piece of piece this repos.
* [zevtyardt](https://github.com/zevtyardt/lk21) for direct links module.
