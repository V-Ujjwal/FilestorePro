#@MxA_Bots | @iSmartBoi_Ujjwal

import os
from os import environ
import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

DELETE_TIME = int(environ.get("DELETE_TIME"))
AUTODELETE_MESSAGE = os.getenv("from os import environ", '''‼️ File will auto delete in few seconds😱 💡Forward it to saved massages or anywhere before downloading.😁 😇Join @(UPDATES_CHANNEL_USERNAME)''')

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"(AUTODELETE_MESSAGE)",
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await reply_forward(message, file_id)


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)

        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await message.reply_text(f'AUTODELETE_MESSAGE')
    asyncio.sleep(DELETE_TIME)
    await sent_message.delete()
