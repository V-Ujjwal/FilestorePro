from aiohttp import web
import asyncio, logging, aiohttp, traceback
#from configs import URL

URL = ""

r = web.RouteTableDef()

@r.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("I am Alive")
  
async def web_server():
    wap = web.Application(client_max_size=30000000)
    wap.add_routes(r)
    return wap

async def ping_server():
    while True:
        await asyncio.sleep(600)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(URL) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()
