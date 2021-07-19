
## About Repo
This repo based [GautamKumar](https://github.com/gautamajay52/TorrentLeech-Gdrive) TorrentLeech with some tweaks

### Tweaks
- Support thumbnail AVI, MOV, 3GP, etc. even you must download the file first
- Add aria2 advance configuration
- Support hxfile, anonfiles, letsupload, etc. based [zevtyardt](https://github.com/zevtyardt/lk21) module
- Simply status messages

### Branch
- Master branch is development version
- Stable branch is stable version

### Direct Links Supports
```
'zippyshare.com', 'yadi.sk', 'cloud.mail.ru', 'mediafire.com', 'osdn.net', 
'github.com', 'racaty.net', 'letsupload.io', 'hxfile.co', 'layarkacaxxi.icu',
'naniplay.nanime.in', 'naniplay.nanime.biz', 'naniplay.com', 'femax20.com',
'anonfiles.com', 'sbembed.com', 'streamsb.net', 'fembed.com', '1drv.ms aka OneDrive'
```
> Note: if you want to mirroring fembed links, use must add https:// in front of links. ex: /mirror https://fembed.com/f/jgndzfdj-n7zyg5
### Thumbnail supports
```
"MKV", "MP4", "WEBM", "AVI", "MOV", 
"MPEG", "WMV", "M4V", "3GP"
```
> Note: Even stream format is support thumbnail, but telegram only support mp4 and mkv thumbnail for stream directly in app. You can still see thumbnail, but you must download the media file when you want to watch or open it.

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
ytleech - Single video Youtube downloader to Telegram.
ytdlsync - Single video Youtube downloader to Drive.
getsize - Get size folder in Drive.
renewme - Cancel all download process.
pytleech - Youtube downloader and send video/music to telegram.
pytdlsync - Youtube downloader and send video/music to Drive.
upload - Hmmm... wait
ytdl - This will download and upload to your Drive.
ytpl - This download youtube playlist and upload to your Drive.
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
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Credits
* [GautamKumar](https://github.com/gautamajay52/TorrentLeech-Gdrive) for original source
* [SlamMirror](https://github.com/breakdowns/slam-mirrorbot) I pick piece of piece this repos