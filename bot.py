import asyncio
import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")

GROUP_IDS = [
    -1001719475141,
    -1003740539352,
    -1002971676598,
    -1002514242670,
    -1003101724935,
    -1003772787120,
    -1003520088160,
    -1002591670499,
    -1002022668873
]

async def main():
    bot = Bot(TOKEN)

    for gid in GROUP_IDS:
        try:
            await bot.send_message(
                chat_id=gid,
                text="Test"
            )
            print(f"OK: {gid}")

        except Exception as e:
            print(f"FEL: {gid} -> {e}")

asyncio.run(main())
