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

### Command
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

### Thumbnail supports
```
"MKV", "MP4", "WEBM", "AVI", "MOV", 
"MPEG", "WMV", "M4V", "3GP"
```
> Note: Even thumbnail support, telegram only support mp4 and mkv for stream directly in app.

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
* [yasirarism](https://github.com/yasirarism) for direct link support
* [SlamMirror](https://github.com/breakdowns/slam-mirrorbot) I pick piece of this repos
* [P3TERX](https://github.com/P3TERX/) for advance aria config