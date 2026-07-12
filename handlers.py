from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

keyboard = [
    ["✈️ دوره‌های آموزشی"],
    ["💰 شهریه دوره‌ها", "📝 ثبت‌نام"],
    ["📍 آدرس", "📞 تماس با ما"],
    ["🌐 وب‌سایت"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛩️ به ربات رسمی مرکز آموزش خلبانی پویا اطلس خوش آمدید.\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید.",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "✈️ دوره‌های آموزشی":
        await update.message.reply_text(
            """✈️ دوره‌های آموزشی پویا اطلس

📚 دوره زمینی (Ground School)

• آیرودینامیک
• هواشناسی
• ناوبری
• قوانین هوانوردی
• مخابرات
• سیستم‌های هواپیما
• عوامل انسانی

──────────────────

🛩️ دوره پرواز (Flight Training)

• آموزش مقدماتی
• تاکسی
• برخاست و فرود
• مانورهای پروازی
• پرواز Solo
• ناوبری
• آمادگی آزمون عملی

تمام آموزش‌ها مطابق استانداردهای سازمان هواپیمایی کشوری انجام می‌شود.
"""
        )

    elif text == "💰 شهریه دوره‌ها":
        await update.message.reply_text(
            """💰 شهریه دوره‌های آموزش خلبانی

📚 دوره زمینی

این دوره شامل آموزش کامل مباحث تئوری مورد نیاز خلبانی است.

✅ سرفصل‌ها
✈️ آیرودینامیک
🌦️ هواشناسی
🧭 ناوبری
📡 مخابرات
⚖️ قوانین هوانوردی
🔧 سیستم‌های هواپیما
👨‍✈️ عوامل انسانی

──────────────────

🛩️ دوره پرواز

این دوره شامل آموزش عملی پرواز با هواپیمای فوق سبک است.

✅ آموزش‌ها

🛫 آشنایی با هواپیما
🛫 چک قبل از پرواز
🛫 تاکسی
🛫 تیک‌آف
🛫 فرود
🛫 مانورهای پروازی
🛫 پرواز Solo
🛫 ناوبری

──────────────────

💳 برای اطلاع از شهریه روز، شرایط پرداخت اقساط و تخفیف‌های ویژه با آموزشگاه تماس بگیرید.

☎️ 02634490401

🌐 https://pooyaflight.com

📷 Instagram: @M.pilot.r
"""
        )

    elif text == "📝 ثبت‌نام":
        await update.message.reply_text(
            """📝 ثبت‌نام

جهت ثبت‌نام در دوره‌های آموزش خلبانی لطفاً با کارشناسان ما تماس بگیرید.

☎️ 02634490401

یا به وب‌سایت مراجعه کنید:

🌐 https://pooyaflight.com
"""
        )

    elif text == "📍 آدرس":
        await update.message.reply_text(
            """📍 آدرس آموزشگاه

استان البرز
فرودگاه آزادی
مرکز آموزش خلبانی پویا اطلس
"""
        )

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            """☎️ تماس با ما

تلفن:
02634490401
09124905605

وب‌سایت:
https://pooyaflight.com

اینستاگرام:
@M.pilot.r
"""
        )

    elif text == "🌐 وب‌سایت":
        await update.message.reply_text(
            "🌐 https://pooyaflight.com"
        )

    else:
        await update.message.reply_text(
            "لطفاً یکی از گزینه‌های منو را انتخاب کنید."
        )
