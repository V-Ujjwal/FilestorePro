import os, logging, asyncio
from aiohttp import web
from pyrogram import Client
from configs import *
from server import web_server

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("Filestore")

class Filestore(Client):
    
    def __init__(self):
        super().__init__(
            "Filestore",
            in_memory=True,
            workers=500,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins")
        )

    async def start(self):
        await super().start()
        logger.info("Bot Started successfully..😎🤏")
        app = web.AppRunner(await web_server())
        await app.setup()
        ba = "0.0.0.0"
        await web.TCPSite(app, ba, 8080).start()

    async def stop(self, *args):
        await super().stop()
        logger.info("Bot Stopped")

if __name__ == '__main__':
    Filestore().run()
