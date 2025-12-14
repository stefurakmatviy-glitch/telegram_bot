from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["TOKEN"]

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Правила чату", url="https://pastebin.com/SaYSTsFW")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Here chat rules",
        reply_markup=reply_markup
    )

async def shluhi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "+79140598671 her name Olezhka!"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("rules", rules))
app.add_handler(CommandHandler("shluhi", shluhi_command))

print("Бот запущений. Чекаю команди /rules або /shluhi …")
app.run_polling()

