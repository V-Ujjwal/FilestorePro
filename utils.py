#@MxA_Bots | @iSmartBoi_Ujjwal
import logging 
import aiohttp 
import os
from os import environ 
from pyrogram.types import *
from pyrogram.errors import *
from pyrogram import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

URL_SHORTENR_WEBSITE = environ.get('SHORT_URL', '')
URL_SHORTNER_WEBSITE_API = environ.get('SHORTAPI', '')

                
async def get_shortlink(link):   
        https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)
    url = f'https://{SHORT_URL}/api'
     SHORT_API,
      'url': link,
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                data = await response.json()
                if data["status"] == "success":
                    return data['shortenedUrl']
                else:
                    logger.error(f"Error: {data['message']}")
                    return link
    except Exception as e:
        logger.error(e)
        return link
