import asyncio
import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")

async def main():
    bot = Bot(TOKEN)
    me = await bot.get_me()
    print(me)

asyncio.run(main())
            
