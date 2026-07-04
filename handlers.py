from telegram import Update
from telegram.ext import ContextTypes
from telegram import ReplyKeyboardMarkup
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
keyboard = [
    ["✈️ دوره‌های آموزشی"],
    ["💰 شهریه", "📝 ثبت‌نام"],
    ["📍 آدرس", "📞 تماس"],
    ["🌐 وبسایت"],
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛩 دوره‌های آموزشی":
        await update.message.reply_text(
            """🛩 دوره‌های آموزشی

✈️ خلبانی فوق سبک
👨‍✈️ آموزش تئوری
🛩 آموزش عملی"""
        )

    elif text == "💰 شهریه":
        await update.message.reply_text(
            "برای اطلاع از شهریه با آموزشگاه تماس بگیرید."
        )

    elif text == "📝 ثبت‌نام":
        await update.message.reply_text(
            "جهت ثبت‌نام با آموزشگاه تماس بگیرید."
        )

    elif text == "📍 آدرس":
        await update.message.reply_text(
            "استان البرز، فرودگاه آزادی، آموزشگاه خلبانی پویا فلایت"
        )

    elif text == "📞 تماس":
        await update.message.reply_text(
            "02634490401"
        )

    elif text == "🌐 وبسایت":
        await update.message.reply_text(
            "https://pooyaflight.com"
        )
