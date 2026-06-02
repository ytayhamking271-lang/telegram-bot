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
    -1002022668873,
    -1002398864983,
    -1003729495750,
    -1003823759558,
    -1003878698570,
    -1002776935595,
    -1002166077462,
    -1003880313099,
    -1002204829364,
    -1001930860839,
    -1002281459943,
    -1002861854715,
    -1003571356874,
    -1003994644272,
    -1002511920553,
    -1001693541154,
    -1003736561695,
    -1003903927647,
    -1003727084067,
    -1003862369106,
    -1003543059399,
    -1003895352194
]

MESSAGE = """
‼️‼️HELT ANONYMA BETALNINGAR

(Via paypal,klarna,apple pay,kort)

Grupper finns få grupperna direkt när betalning är gjort om vi inte svarar😊

 • 1 GRUPP (https://telegram-grupper-2.myshopify.com/products/1-gruppsvensk)

 • 5 GRUPPER (https://telegram-grupper-2.myshopify.com/products/utan-namn-28feb-_12-38)

 • DANSKED EXPOSÉ (https://telegram-grupper-2.myshopify.com/products/1-danmark-group)

@ghettograbb2 @ghettograbb3
"""

bot = Bot(token=TOKEN)

async def send_to_groups():
    while True:
        for group_id in GROUP_IDS:
            try:
                await bot.send_message(
                    chat_id=group_id,
                    text=MESSAGE
                )

                print(f"Skickat till grupp {group_id}")

                await asyncio.sleep(2)

            except Exception as e:
                print(f"Fel i grupp {group_id}: {e}")

        print("Klar. Väntar 1 timme...")
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(send_to_groups())
