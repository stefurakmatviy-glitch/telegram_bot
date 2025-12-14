from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Беремо токен з Environment Variable
TOKEN = os.environ["TOKEN"]

# Команда /rules
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📜 Правила чату", url="https://pastebin.com/SaYSTsFW")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Ось правила чату",
        reply_markup=reply_markup
    )

# Команда /shluhi
async def shluhi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Наразі єдина вільна шлюха Олєжка, її номер +79140598671"
    )

# Створюємо додаток та додаємо обробники команд
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("rules", rules))
app.add_handler(CommandHandler("shluhi", shluhi_command))

print("Бот запущений. Чекаю команди /rules або /shluhi …")
app.run_polling()

import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

PORT = int(os.environ.get("PORT", 8080))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    httpd = HTTPServer(('0.0.0.0', PORT), Handler)
    httpd.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

