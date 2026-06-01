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
    -1002776935595
]

MESSAGE = """
🚨 ALLA SVENSKA STÄDER FINNS TILLGÄNGLIGA 🚨

✅ 250 000+ videor/bilder
✅ 150+ grupper
✅ Städer över hela Sverige
✅ Direkt leverans efter betalning

📩 Vid intresse: @ghettograbb2

💳 Helt anonyma betalningar via:
• PayPal
• Klarna
• Apple Pay
• Kort

🛒 Köp direkt:

• 1 Grupp:
https://telegram-grupper-2.myshopify.com/products/1-gruppsvensk

• 5 Grupper:
https://telegram-grupper-2.myshopify.com/products/utan-namn-28feb-_12-38

• Dansk Exposé:
https://telegram-grupper-2.myshopify.com/products/1-danmark-group

🤖 Ny bot tillgänglig:
@Svenska_grupper_bot

Boten känner automatiskt av när någon går med via din länk – du behöver inte längre kontrollera manuellt.

⚡ Om vi inte svarar direkt kan du köpa via länkarna ovan och få tillgång snabbare.

📩 Kontakta:
@ghettograbb2
@ghettograbb3
"""

bot = Bot(token=TOKEN)

async def send_to_groups():

    while True:

        print("Skickar meddelanden...")

        for group_id in GROUP_IDS:

            try:

                await bot.send_message(

                    chat_id=group_id,

                    text=MESSAGE

                )

                print(f"Skickat till grupp {group_id}")

                # Vänta lite mellan varje grupp

                await asyncio.sleep(2)

            except Exception as e:

                print(f"Fel i grupp {group_id}: {e}")

        print("Klar. Väntar 5 minuter...")

        await asyncio.sleep(300)

if __name__ == "__main__":

    asyncio.run(send_to_groups())
