from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import asyncio


TOKEN = "8676435910:AAGDgHikdhj3e6M_WtStExPjXWjZAvl4PTs"

PHOTO_URL = "https://i.ibb.co/S466K0H7/ksenia102.jpg"


last_trigger_time = 0
LOCK = asyncio.Lock()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_trigger_time

    if update.message and update.message.text:
        text = update.message.text.strip().lower()
        if text == "ксюша":
            async with LOCK:
                current_time = asyncio.get_event_loop().time()
                if current_time - last_trigger_time >= 30:
                    last_trigger_time = current_time
                    await update.message.reply_photo(photo=PHOTO_URL)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
app.run_polling()
