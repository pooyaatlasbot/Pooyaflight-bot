from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import TOKEN
from handlers import start, menu
from database import init_db







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
init_db()

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

app.run_polling()
