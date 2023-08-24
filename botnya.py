import asyncio
from ubot import *

async def main():
    await bot.start()
    try:
        await loadPlugins()
        await expiredUserbots()
        await installPeer()
        if "test" not in sys.argv:
            await bot.idle()
    except KeyboardInterrupt:
        logger.warning("BOT STOP....")
    finally:
        await bot.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())