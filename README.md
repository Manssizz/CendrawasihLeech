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
zippyshare.com, yadi.sk, cloud.mail.ru, mediafire.com, osdn.net, 
github.com, racaty.net, letsupload.io, hxfile.co, anonfiles.com,
bayfiles.com, antfiles.com, streamtape.com, 1drv.ms aka OneDrive,
mxplayer.in, pixledrain.com, solidfiles.com, pixeldrain.com

- Fembed with mirror domain
naniplay.nanime.in, naniplay.nanime.biz, naniplay.com, femax20.com,
feurl.com, fcdn.stream, layarkacaxxi.icu

- StreamSB with mirror domain
sbembed.com, sbembed1.com, sbembed2.com, sbembed3.com, sbembed4.com
sbplay.org, sbplay.one, streamsb.net, sbcloud1.com
```
> Note: if you want to mirroring fembed links, use must add https:// in front of links. ex: /mirror https://fembed.com/f/jgndzfdj-n7zyg5
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
> `Important:` **Because personal data login is a very confidential thing, i exclude my .netrc file in gitignore. if you want add, remove netrc in gitignore and  make you repo private before you push .netrc file** 
### Sample of rClone config
<h1 align="center">
  <a href="https://github.com/Manssizz/CendrawasihLeech"><img src="https://raw.githubusercontent.com/Manssizz/CendrawasihLeech/master/rclone.jpg" alt="rClone config"></a>
</h1>

### Command List
```
leech - Leech torrent file or direct link file and upload to Telegram.
clone - Clone Drive file or folder to your Drive.
sync - Leech torrent/direct link to Drive.
tgsync - This will mirror the telegram files to ur Drive.
archive - Leech torrent file or direct link file and upload to Telegram and upload as archive file.
extract - This will unarchive file and upload to telegram.
log - This will send you a txt file of the logs.
status - Get download/upload process status. 
stop - Stop single process command 
tarsync - This command will compress the folder/file and will upload to Drive.
untarsync - This will unarchive file and upload to Drive.
tguntar - This will unarchive telegram file and upload to cloud.
ytdl - Single video Youtube downloader to Telegram.
ytdlsync - Single video Youtube downloader to Drive.
pytleech - Youtube downloader and send video/music to telegram.
pytdlsync - Youtube downloader and send video/music to Drive.
getsize - Get size folder in Drive.
renewme - Cancel all download process.
upload - Hmmm... wait
rclone - This will change your drive config on fly.(First one will be default)
rename - To rename the telegram files.
```

### Archive supports
```
ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2, 
APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT, 
HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, 
NTFS, RPM, SquashFS, UDF, VHD, XAR, Z.
```

### Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Manssizz/CendrawasihLeech/tree/stable)

### Credits
* [GautamKumar](https://github.com/gautamajay52/TorrentLeech-Gdrive) for original source
* [SlamMirror](https://github.com/breakdowns/slam-mirrorbot) I pick piece of piece this repos
