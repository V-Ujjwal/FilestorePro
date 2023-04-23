#@MxA_Bots | @iSmartBoi_Ujjwal

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
import time

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"**Files will be Deleted After few seconds ⏰**\n",
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


async def delete_file(file_id: int):
    await asyncio.sleep(20)  # wait for 20 seconds
    # Delete the file using the file ID
    # Code to delete the file goes here


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    await asyncio.create_task(delete_file(file_id)) # schedule the file deletion task
else:
async def send_files(bot, chat_id, file_ids):
    for file_id in file_ids:
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_DOCUMENT)
        bot.send_document(chat_id=chat_id, document=file_id)
        # Wait for 30 seconds before sending the next file
        time.sleep(30)

    # Delete all files after the last file has been sent
    for file_id in file_ids:
        bot.delete_message(chat_id=chat_id, message_id=file_id)
