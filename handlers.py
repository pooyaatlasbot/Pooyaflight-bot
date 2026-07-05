from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

keyboard = [
    ["✈️ دوره‌های آموزشی"],
    ["💰 شهریه", "📝 ثبت‌نام"],
    ["📍 آدرس", "📞 تماس با ما"],
    ["🌐 وب‌سایت"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛩 به ربات رسمی مرکز آموزش خلبانی پویا اطلس خوش آمدید.",
        reply_markup=reply_markup
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "✈️ دوره‌های آموزشی":
        await update.message.reply_text(
            "✈️ دوره خلبانی فوق سبک\n"
            "👨‍✈️ آموزش تئوری\n"
            "🛩 آموزش عملی"
        )

    elif text == "💰 شهریه":
        await update.message.reply_text(
            "برای اطلاع از شهریه با آموزشگاه تماس بگیرید."
        )

    elif text == "📝 ثبت‌نام":
        await update.message.reply_text(
            "جهت ثبت‌نام با شماره 02634490401 تماس بگیرید."
        )

    elif text == "📍 آدرس":
        await update.message.reply_text(
            "استان البرز، فرودگاه آزادی، مرکز آموزش خلبانی پویا اطلس"
        )

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            "02634490401"
        )

    elif text == "🌐 وب‌سایت":
        await update.message.reply_text(
            "https://pooyaflight.com"
        )