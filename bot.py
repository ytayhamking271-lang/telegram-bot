import asyncio
import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")

GROUP_ID = -1001719475141

async def main():
    bot = Bot(TOKEN)

    msg = await bot.send_message(
        chat_id=GROUP_ID,
        text="Test från Railway"
    )

    print(msg)

asyncio.run(main())
