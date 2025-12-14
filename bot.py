import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ========================
# Налаштування бота
# ========================
TOKEN = os.environ["TOKEN"]
APP_URL = os.environ["APP_URL"]  # Наприклад: https://telegram1488.fly.dev

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

# ========================
# Створюємо додаток
# ========================
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("rules", rules))
app.add_handler(CommandHandler("shluhi", shluhi_command))

# ========================
# Keep-alive сервер для Fly
# ========================
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

# ========================
# Запускаємо webhook
# ========================
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=APP_URL + "/"
)

print("Бот запущений через webhook і готовий до команд!")


