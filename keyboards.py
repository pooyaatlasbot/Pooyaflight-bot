from telegram import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    [
        ["✈️ دوره‌های آموزشی", "💰 شهریه دوره‌ها"],
        ["📝 ثبت‌نام", "📍 آدرس آموزشگاه"],
        ["☎️ تماس با ما", "🌐 وب‌سایت"],
        ["📷 اینستاگرام"]
    ],
    resize_keyboard=True
)
