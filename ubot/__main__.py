import asyncio
import importlib
from importlib import import_module
from pyrogram import idle
from pyrogram.errors import RPCError

from ubot import *
from ubot.modules import loadModule



async def auto_restart():
    while not await asyncio.sleep(90):
        def _():
            os.system(f"kill -9 {os.getpid()} && python3 -m ubot")
        sys.exit(0)


async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
        await ubot_.join_chat("xCodee1")
        await ubot_.join_chat("zasupport")
        await ubot_.join_chat("kynansupport")
        await ubot_.join_chat("anothrllv")
        await ubot_.join_chat("PesulapTelegram")
    except asyncio.TimeoutError:
        #await remove_ubot(user_id)
        await add_prem(user_id)
        await sending_user(user_id)
        print(f"✅ {user_id} Gak Respon.")
    except RPCError:
        #await remove_ubot(user_id)
        #await rm_all(user_id)
        #await rem_expired_date(user_id)
        #for X in await get_chat(user_id):
            #await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")
    except:
        pass


async def main():
    userbots = await get_userbots()
    tasks = [
        start_ubot(int(_ubot["name"]), _ubot)
        for _ubot in userbots
    ]
    await asyncio.gather(*tasks)
    await bot.start()
    #auto_restart(),
    await asyncio.gather(loadPlugins(), installPeer(), auto_restart(), expiredUserbots(), idle())


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())