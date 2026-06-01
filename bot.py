import asyncio
import os
from telegram import Bot
TOKEN = os.getenv("TOKEN")
GROUP_IDS = [
    -1001719475141
]
MESSAGE = "Hej"
bot = Bot(token=TOKEN)
async def main():
    while True:
        for group_id in GROUP_IDS:
            try:
                await bot.send_message(
                    chat_id=group_id,
                    text=MESSAGE
                )

                print(f"Skickat till {group_id}")

            except Exception as e:
                print(f"Fel i {group_id}: {e}")

            await asyncio.sleep(2)

        print("Väntar 5 minuter...")
        await asyncio.sleep(300)

asyncio.run(main())
