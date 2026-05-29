from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEST_CHAT = os.getenv("DEST_CHAT")

SIGNAL_TAG = "#SIGNAL"

async def filter_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if not message or not message.text:
        return

    text = message.text.strip()

    if SIGNAL_TAG not in text:
        return

    clean_text = text.replace(SIGNAL_TAG, "").strip()

    await context.bot.send_message(
        chat_id=DEST_CHAT,
        text=clean_text
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.UpdateType.CHANNEL_POST & filters.TEXT, filter_signal)
    )

    print("Bot avviato correttamente")

    app.run_polling()

if __name__ == "__main__":
    main()
