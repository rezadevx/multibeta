import asyncio
import importlib
from importlib import import_module
from pyrogram import idle
from pyrogram.errors import RPCError

from ubot import *
from ubot.modules import loadModule

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
        LOGGER("Info").info(f"[𝗜𝗡𝗙𝗢] - ({user_id}) 𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")
    except RPCError:
        #await remove_ubot(user_id)
        #await rm_all(user_id)
        #await rem_expired_date(user_id)
        #for X in await get_chat(user_id):
            #await remove_chat(user_id, X)
        LOGGER("Warning").warning(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")
    except:
        pass


async def main():
    tasks = [
        asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    LOGGER("Info").info(f"Starting Bot")
    await asyncio.gather(*tasks, bot.start())
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())



if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())