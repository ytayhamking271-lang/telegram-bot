import asyncio
import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")

GROUP_IDS = [
    -1001719475141,
    -1002318437904,
    -1002450763132,
    -1003740539352,
    -1002630229848,
    -1003919199766,
    -1003729495750,
    -1003520088160,
    -1003126524114,
    -1001755122717
]

async def main():
    bot = Bot(TOKEN)

    for gid in GROUP_IDS:
        try:
            msg = await bot.send_message(
                chat_id=gid,
                text="Test"
            )
            print(f"OK: {gid}")

        except Exception as e:
            print(f"FEL: {gid} -> {e}")

asyncio.run(main())
