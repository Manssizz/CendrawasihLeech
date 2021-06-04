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
        Available Commands:
        /leech - Leech torrent file or direct link file and upload to Telegram.
        /clone - Clone Drive file or folder to your Drive.
        /sync - Leech torrent/direct link to Drive.
        /tgsync - This will mirror the telegram files to ur Drive.
        /log - This will send you a txt file of the logs.
        /status - Get download/upload process status. 
        /stop - Stop single process command 
        /tarleech - Leech torrent file or direct link file and upload to Telegram and upload as archive file.
        /tarsync - This command will compress the folder/file and will upload to Drive.
        /leechuntar - This will unarchive file and upload to telegram.
        /untarsync - This will unarchive file and upload to Drive.
        /tguntar - This will unarchive telegram file and upload to cloud.
        /ytleech - Single video Youtube downloader to Telegram.
        /ytdlsync - Single video Youtube downloader to Drive.
        /getsize - Get size folder in Drive.
        /renewme - Cancel all download process.
        /pytleech - Youtube downloader and send video/music to telegram.
        /pytdlsync - Youtube downloader and send video/music to Drive.
        /upload - Hmmm... wait
        /ytdl - This will download and upload to your Drive.
        /ytpl - This download youtube playlist and upload to your Drive.
        /rclone - This will change your drive config on fly.(First one will be default)
        /rename - To rename the telegram files.
        """,
        disable_web_page_preview=True)
