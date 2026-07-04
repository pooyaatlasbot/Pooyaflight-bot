from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os
from config import ADMIN_ID
from keyboards import main_keyboard
from database import init_db
from handlers import start, menu
TOKEN = os.getenv("BOT_TOKEN")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛩️ به ربات رسمی آموزشگاه خلبانی پویا فلایت خوش آمدید.",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "✈️ دوره‌های آموزشی":
        await update.message.reply_text(
            "✈️ آموزش خلبانی فوق سبک\n"
            "👨‍✈️ آموزش تئوری\n"
            "🛩️ آموزش عملی"
        )

    elif text == "🌐 وب‌سایت":
        await update.message.reply_text("https://pooyaflight.ir")

    elif text == "📞 تماس با ما":
        await update.message.reply_text("02634490401")

    elif text == "📍 آدرس":
        await update.message.reply_text(
            "استان البرز - فرودگاه آزادی - آموزشگاه خلبانی پویا فلایت"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

app.run_polling()
