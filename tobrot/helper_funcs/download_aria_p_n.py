#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

import asyncio
import logging
import os
import sys
import time
import requests

import aria2p
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from tobrot import (
    # ARIA_TWO_STARTED_PORT,
    AUTH_CHANNEL,
    CUSTOM_FILE_NAME,
    DOWNLOAD_LOCATION,
    EDIT_SLEEP_TIME_OUT,
    LOGGER,
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START,
)
from tobrot.helper_funcs.create_compressed_archive import (
    create_archive,
    get_base_name,
    unzip_me,
)
from tobrot.helper_funcs.extract_link_from_message import extract_link
from tobrot.helper_funcs.upload_to_tg import upload_to_gdrive, upload_to_tg
from tobrot.helper_funcs.direct_link_generator import direct_link_generator
from tobrot.helper_funcs.exceptions import DirectDownloadLinkException

sys.setrecursionlimit(10 ** 4)

def KopyasizListe(string):
    kopyasiz = list(string.split(","))
    kopyasiz = list(dict.fromkeys(kopyasiz))
    return kopyasiz


def Virgullustring(string):
    string = string.replace("\n\n", ",")
    string = string.replace("\n", ",")
    string = string.replace(",,", ",")
    string = string.rstrip(',')
    string = string.lstrip(',')
    return string


tracker_urlsss = [
    "https://newtrackon.com/api/all"
    # "https://trackerslist.com/all.txt"
    "https://trackerslist.com/best.txt"
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all.txt"
]
tumtorrenttrackerstringi = ""
sonstringtrckr = ""
for i in range(len(tracker_urlsss)):
    response = requests.get(tracker_urlsss[i])
    response.encoding = "utf-8"
    tumtorrenttrackerstringi += "\n"
    tumtorrenttrackerstringi += response.text
trackerlistemiz = KopyasizListe(Virgullustring(tumtorrenttrackerstringi))
sonstringtrckr = ','.join(trackerlistemiz)
# LOGGER.info(sonstringtrckr)
# trackelreri alıyoz dinamik olarak

async def aria_start():
    global sonstringtrckr
    aria2_daemon_start_cmd = []
    # start the daemon, aria2c command
    aria2_daemon_start_cmd.append("aria2c")
    aria2_daemon_start_cmd.append("--allow-overwrite=true")
    aria2_daemon_start_cmd.append("--daemon=true")
    aria2_daemon_start_cmd.append("--check-certificate=false")
    # aria2_daemon_start_cmd.append("--enable-dht")
    # aria2_daemon_start_cmd.append("--dht-listen-port=6881")
    aria2_daemon_start_cmd.append("--follow-metalink=mem")
    aria2_daemon_start_cmd.append("--bt-max-peers=0")
    aria2_daemon_start_cmd.append("--seed-time=0.01")
    aria2_daemon_start_cmd.append("--min-split-size=10M")
    aria2_daemon_start_cmd.append("--peer-id-prefix=-qB4341-")
    aria2_daemon_start_cmd.append("--user-agent=qBittorrent/4.3.4.1")
    aria2_daemon_start_cmd.append("--disk-cache=64M")
    aria2_daemon_start_cmd.append("--file-allocation=prealloc")
    aria2_daemon_start_cmd.append("--continue=true")
    aria2_daemon_start_cmd.append("--bt-request-peer-speed-limit=2048K")
    aria2_daemon_start_cmd.append("--auto-file-renaming=true")
    aria2_daemon_start_cmd.append("--max-tries=20")
    aria2_daemon_start_cmd.append("--bt-enable-lpd=true")
    aria2_daemon_start_cmd.append("--seed-ratio=0.0")
    aria2_daemon_start_cmd.append("--content-disposition-default-utf8=true")
    aria2_daemon_start_cmd.append("--http-accept-gzip=true")
    aria2_daemon_start_cmd.append("--reuse-uri=true")
    aria2_daemon_start_cmd.append("--max-file-not-found=5")
    aria2_daemon_start_cmd.append("--follow-torrent=mem")
    aria2_daemon_start_cmd.append("--max-connection-per-server=10")
    aria2_daemon_start_cmd.append("--min-split-size=10M")
    aria2_daemon_start_cmd.append("--enable-rpc")
    aria2_daemon_start_cmd.append("--rpc-listen-all=false")
    aria2_daemon_start_cmd.append("--rpc-listen-port=8100")
    aria2_daemon_start_cmd.append("--rpc-max-request-size=1024M")
    aria2_daemon_start_cmd.append("--seed-time=0")
    aria2_daemon_start_cmd.append("--max-overall-upload-limit=1K")
    aria2_daemon_start_cmd.append("--split=10")
    aria2_daemon_start_cmd.append(f"--bt-tracker={sonstringtrckr}")
    #
    LOGGER.info(aria2_daemon_start_cmd)
    #
    process = await asyncio.create_subprocess_exec(
        *aria2_daemon_start_cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    LOGGER.info(stdout)
    LOGGER.info(stderr)
    aria2 = aria2p.API(
        aria2p.Client(host="http://localhost", port=8100, secret="")
    )
    return aria2


def add_magnet(aria_instance, magnetic_link, c_file_name):
    options = None
    # if c_file_name is not None:
    #     options = {
    #         "dir": c_file_name
    #     }
    try:
        download = aria_instance.add_magnet(magnetic_link, options=options)
    except Exception as e:
        return (
            False,
            "**FAILED** \n" + str(e) + " \nPlease don't send slow torrent links",
        )
    else:
        return True, "" + download.gid + ""


def add_torrent(aria_instance, torrent_file_path):
    if torrent_file_path is None:
        return (
            False,
            "**FAILED**"
            + str(e)
            + " \nFailed to getting data <u>Torrent</u> file.",
        )
    if os.path.exists(torrent_file_path):
        # Add Torrent Into Queue
        try:
            download = aria_instance.add_torrent(
                torrent_file_path, uris=None, options=None, position=None
            )
        except Exception as e:
            return (
                False,
                "**FAILED**"
                + str(e)
                + " \nTolong jangan menggunakan link lambat",
            )
        else:
            return True, "" + download.gid + ""
    else:
        return False, "**FAILED** \nPlease try another source links"


def add_url(aria_instance, text_url, c_file_name):
    options = None
    # if c_file_name is not None:
    #     options = {
    #         "dir": c_file_name
    #     }
    if "zippyshare.com" in text_url \
        or "osdn.net" in text_url \
        or "mediafire.com" in text_url \
        or "cloud.mail.ru" in text_url \
        or "github.com" in text_url \
        or "yadi.sk" in text_url  \
        or "letsupload.io" in text_url  \
        or "hxfile.co" in text_url  \
        or "layarkacaxxi.icu" in text_url  \
        or "femax20.com" in text_url  \
        or "anonfiles.com" in text_url  \
        or "racaty.net" in text_url:
            try:
                urisitring = direct_link_generator(text_url)
                uris = [urisitring]
            except DirectDownloadLinkException as e:
                LOGGER.info(f'{text_url}: {e}')
    else:
        uris = [text_url]
    # Add URL Into Queue
    try:
        download = aria_instance.add_uris(uris, options=options)
    except Exception as e:
        return (
            False,
            "**FAILED** \n" + str(e) + " Slow link detect",
        )
    else:
        return True, "" + download.gid + ""


async def call_apropriate_function(
    aria_instance,
    incoming_link,
    c_file_name,
    sent_message_to_update_tg_p,
    is_zip,
    cstom_file_name,
    is_cloud,
    is_unzip,
    user_message,
    client,
):
    if incoming_link.lower().startswith("magnet:"):
        sagtus, err_message = add_magnet(aria_instance, incoming_link, c_file_name)
    elif incoming_link.lower().endswith(".torrent"):
        sagtus, err_message = add_torrent(aria_instance, incoming_link)
    else:
        sagtus, err_message = add_url(aria_instance, incoming_link, c_file_name)
    if not sagtus:
        return sagtus, err_message
    LOGGER.info(err_message)
    # https://stackoverflow.com/a/58213653/4723940
    await check_progress_for_dl(
        aria_instance, err_message, sent_message_to_update_tg_p, None
    )
    if incoming_link.startswith("magnet:"):
        #
        err_message = await check_metadata(aria_instance, err_message)
        #
        await asyncio.sleep(1)
        if err_message is not None:
            await check_progress_for_dl(
                aria_instance, err_message, sent_message_to_update_tg_p, None
            )
        else:
            return False, "Failed to get metadata \n\n#MetaDataError"
    await asyncio.sleep(1)
    file = aria_instance.get_download(err_message)
    to_upload_file = file.name
    com_g = file.is_complete
    #
    if is_zip:
        check_if_file = await create_archive(to_upload_file)
        if check_if_file is not None:
            to_upload_file = check_if_file
    #
    if is_unzip:
        try:
            check_ifi_file = get_base_name(to_upload_file)
            await unzip_me(to_upload_file)
            if os.path.exists(check_ifi_file):
                to_upload_file = check_ifi_file
        except Exception as ge:
            LOGGER.info(ge)
            LOGGER.info(
                f"Can't extract {os.path.basename(to_upload_file)}, Uploading the same file"
            )

    if to_upload_file:
        if CUSTOM_FILE_NAME:
            if os.path.isfile(to_upload_file):
                os.rename(to_upload_file, f"{CUSTOM_FILE_NAME}{to_upload_file}")
                to_upload_file = f"{CUSTOM_FILE_NAME}{to_upload_file}"
            else:
                for root, _, files in os.walk(to_upload_file):
                    LOGGER.info(files)
                    for org in files:
                        p_name = f"{root}/{org}"
                        n_name = f"{root}/{CUSTOM_FILE_NAME}{org}"
                        os.rename(p_name, n_name)
                to_upload_file = to_upload_file

    if cstom_file_name:
        os.rename(to_upload_file, cstom_file_name)
        to_upload_file = cstom_file_name
    #
    response = {}
    LOGGER.info(response)
    user_id = user_message.from_user.id
    if com_g:
        if is_cloud:
            await upload_to_gdrive(
                to_upload_file, sent_message_to_update_tg_p, user_message, user_id
            )
        else:
            final_response = await upload_to_tg(
                sent_message_to_update_tg_p, to_upload_file, user_id, response, client
            )
            if not final_response:
                return True, None
            try:
                message_to_send = ""
                for key_f_res_se in final_response:
                    local_file_name = key_f_res_se
                    message_id = final_response[key_f_res_se]
                    channel_id = str(sent_message_to_update_tg_p.chat.id)[4:]
                    private_link = f"https://t.me/c/{channel_id}/{message_id}"
                    message_to_send += "• <a href='"
                    message_to_send += private_link
                    message_to_send += "'>"
                    message_to_send += local_file_name
                    message_to_send += "</a>"
                    message_to_send += "\n"
                if message_to_send != "":
                    mention_req_user = (
                        f"<a href='tg://user?id={user_id}'>Uploaded</a>\n\n"
                    )
                    message_to_send = mention_req_user + message_to_send
                    message_to_send = message_to_send + "#Uploaded"
                else:
                    message_to_send = "<i>FAILED</i> uploading files."
                await user_message.reply_text(
                    text=message_to_send, quote=True, disable_web_page_preview=True
                )
            except Exception as go:
                LOGGER.error(go)
    return True, None


#


# https://github.com/jaskaranSM/UniBorg/blob/6d35cf452bce1204613929d4da7530058785b6b1/stdplugins/aria.py#L136-L164
async def check_progress_for_dl(aria2, gid, event, previous_message):
    # g_id = event.reply_to_message.from_user.id
    try:
        file = aria2.get_download(gid)
        complete = file.is_complete
        is_file = file.seeder
        if not complete:
            if not file.error_message:
                msg = ""
                # sometimes, this weird https://t.me/c/1220993104/392975
                # error creeps up
                # TODO: temporary workaround
                downloading_dir_name = "N/A"
                try:
                    # another derp -_-
                    # https://t.me/c/1220993104/423318
                    downloading_dir_name = str(file.name)
                except:
                    pass
                #
                if is_file is None:
                    msgg = f"<b>• Connections : {file.connections} </b>"
                else:
                    msgg = f"<b>• Peers:</b> <code>{file.connections}</code> <b>Seeds:</b> <code>{file.num_seeders}</code>\n<b>• GID :</b> <code>{gid}</code>"
                    msg = f"\n<b>• File Name :</b> `{downloading_dir_name}`"
                    msg += f"\n<b>• Speed :</b> <code>{file.download_speed_string()}</code> <b>ETA :</b> <code>{file.eta_string()}</code>"
                    msg += f"\n<b>• Size :</b> <code>{file.total_length_string()}</code>  [<code>{file.progress_string()}</code>]\n{msgg}"
                inline_keyboard = []
                ikeyboard = []
                ikeyboard.append(
                    InlineKeyboardButton(
                        "Cancel", callback_data=(f"cancel {gid}").encode("UTF-8")
                    )
                )
                inline_keyboard.append(ikeyboard)
                reply_markup = InlineKeyboardMarkup(inline_keyboard)
                if msg != previous_message:
                    if not file.has_failed:
                        try:
                            await event.edit(msg, reply_markup=reply_markup)
                        except FloodWait as e_e:
                            LOGGER.warning(f"Trying to sleep for {e_e}")
                            time.sleep(e_e.x)
                        except MessageNotModified as e_p:
                            LOGGER.info(e_p)
                            await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
                        previous_message = msg
                    else:
                        LOGGER.info(
                            f"Cancelling {file.name} \nSlow torrent source detect"
                        )
                        await event.edit(
                            f"Cancelled\n<code>{file.name}</code>\n\n #MetaDataError"
                        )
                        file.remove(force=True, files=True)
                        return False
            else:
                msg = file.error_message
                LOGGER.info(msg)
                await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
                await event.edit(f"`{msg}`")
                return False
            await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
            await check_progress_for_dl(aria2, gid, event, previous_message)
        else:
            LOGGER.info(
                f"<b>Download Successfully</b> \n`{file.name} ({file.total_length_string()})`"
            )
            await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
            await event.edit(
                f"<b>Download Complete</b> \n`{file.name} ({file.total_length_string()})`"
            )
            return True
    except aria2p.client.ClientException:
        await event.edit(
            f"<b>Download cancelled</b> \n<code>> {file.name} ({file.total_length_string()})</code>"
        )
    except MessageNotModified as ep:
        LOGGER.info(ep)
        await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
        await check_progress_for_dl(aria2, gid, event, previous_message)
    except FloodWait as e:
        LOGGER.info(e)
        time.sleep(e.x)
    except RecursionError:
        file.remove(force=True, files=True)
        await event.edit(
            "<b>Download stoped</b> \n"
            "`Timeout was reached.`".format(file.name)
        )
        return False
    except Exception as e:
        LOGGER.info(str(e))
        if "not found" in str(e) or "'file'" in str(e):
            await event.edit(
                f"<b>Download stoped</b> \n<code>{file.name} ({file.total_length_string()})</code>"
            )
            return False
        else:
            LOGGER.info(str(e))
            await event.edit(
                "<u>error</u> :\n<code>{}</code> \n\n#error".format(str(e))
            )
            return False


# https://github.com/jaskaranSM/UniBorg/blob/6d35cf452bce1204613929d4da7530058785b6b1/stdplugins/aria.py#L136-L164


async def check_metadata(aria2, gid):
    file = aria2.get_download(gid)
    LOGGER.info(file)
    if not file.followed_by_ids:
        # https://t.me/c/1213160642/496
        return None
    new_gid = file.followed_by_ids[0]
    LOGGER.info("Changing GID " + gid + " to " + new_gid)
    return new_gid
