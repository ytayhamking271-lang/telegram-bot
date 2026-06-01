import asyncio
from telegram import Bot
TOKEN = "8667987742:AAHJ2bg-yHesjWCMBZCu7LgaZvoCxiL7EAI"
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
MESSAGE = """
━━━━━━━━━━━━━━━━━━━━
🔥 PREMIUM TELEGRAMGRUPPER 🔥
━━━━━━━━━━━━━━━━━━━━
💳 HELT ANONYMA BETALNINGAR
✔ PayPal
✔ Klarna
✔ Apple Pay
✔ Kort
⚡ DIREKT LEVERANS
Få tillgång direkt efter genomförd betalning.
━━━━━━━━━━━━━━━━━━━━
📦 VÅRA PAKET
━━━━━━━━━━━━━━━━━━━━
🔹 1 GRUPP
https://telegram-grupper-2.myshopify.com/products/1-gruppsvensk
🔹 5 GRUPPER
https://telegram-grupper-2.myshopify.com/products/utan-namn-28feb-_12-38
🔹 DANSK EXPOSÉ
https://telegram-grupper-2.myshopify.com/products/1-danmark-group
━━━━━━━━━━━━━━━━━━━━
📩 KONTAKT
━━━━━━━━━━━━━━━━━━━━
👉 @ghettograbb2
👉 @ghettograbb3
━━━━━━━━━━━━━━━━━━━━
✅ Direkt tillgång
✅ Säkra betalningar
✅ Snabb support
🔥 Beställ idag!
━━━━━━━━━━━━━━━━━━━━
"""
bot = Bot(token=TOKEN)
async def main():
    while True:
        for group_id in GROUP_IDS:
            try:
                await bot.send_message(
                    chat_id=group_id,
                    text=MESSAGE,
                    disable_web_page_preview=True
                )
                print(f"Skickat till {group_id}")
            except Exception as e:
                print(f"Fel i {group_id}: {e}")
            await asyncio.sleep(2)
        print("Väntar 5 minuter...")
        await asyncio.sleep(300)
asyncio.run(main())
