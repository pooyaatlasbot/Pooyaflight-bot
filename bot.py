from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import TOKEN
from handlers import start, menu
from database import init_db








init_db()

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

app.run_polling()
