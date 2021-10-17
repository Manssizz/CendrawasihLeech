#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import AUTH_CHANNEL, LOGGER


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help

    await message.reply_text(
        """
<b>CendrawasihLeech Commands:</b>
/leech - Leech and upload to Telegram.
/clone - Clone Drive file or folder.
/sync - Leech torrent/direct link to Drive.
/tgsync - Mirror telegram files to ur Drive.
/log - Check logs.
/status - Get download/upload process status. 
/stop - Stop single process command 
/archive - Leech and upload as archive file on Telegram.
/tarsync - Compress folder/file and upload to Drive.
/extract - Extract file and upload to telegram.
/untarsync - Extract file and upload to Drive.
/tguntar - Extract telegram file and upload to cloud.
/ytdl - Download Youtube video and upload to Telegram.
/ytdlsync - Download Youtube video and upload to Drive.
/getsize - Get size folder in Drive.
/renewme - Cancel all download process.
/pytleech - Youtube playlist downloader and send to telegram.
/pytdlsync - Youtube playlist downloader and send to Drive.
/upload - Hmmm... wait.
/tshelp - Torrent search helper.
/speedtest - Check server connection speed.
/rclone - [Admin Only] Change or edit rClone config.
/rename - To rename the telegram files.
    """,
        disable_web_page_preview=True)
