#Start bot V1
import telebot

first_button = telebot.types.InlineKeyboardButton("چنل موزیک من 😎", url="https://t.me/shahdowooficial011")
tow_button = telebot.types.InlineKeyboardButton("موزیک های من 🤑", callback_data="tow")
three_button = telebot.types.InlineKeyboardButton("حساب کاربری من 🤖", callback_data="three")
for_button = telebot.types.InlineKeyboardButton("راهنما 🙅", callback_data="he")
hmarkup = telebot.types.InlineKeyboardMarkup()
hmarkup.add(for_button)
hmarkup.add(first_button,tow_button)
hmarkup.add(three_button)


bot = telebot.TeleBot("8355544886:AAGWSNGEdsWR-P-U00fDNeZsahYV-iib8bE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, action='typing')
    bot.reply_to(message, f"سلام {message.chat.first_name}, به ربات شادو موزیک خوش امدید 🤩", reply_markup=hmarkup)

@bot.message_handler(commands=['track1'])
def send_1(message):
    bot.reply_to(message, "خواننده : علی سورنا \n عکس اهنگ در پیام بعد به همراه موزیک ")
    bot.send_photo(message.chat.id, open('ali.jpg', 'rb'))
    bot.send_audio(message.chat.id, open('track1.mp3', 'rb'))
@bot.callback_query_handler(func=lambda call: True)
def send_buuton(call):
    if call.data == "tow":
        bot.reply_to(call.message, "سلام رفیق به بخش موزیک های من خوش امدی 😯\n برای دیدن اولین ترک من به نام خاک این رو بزن /track1")
    elif call.data == "three":
        bot.reply_to(call.message, f"به بخش حساب کاربری شادو موزیک خوش امدید \n اسم شما {call.message.chat.first_name}\n فامیلی شما : {call.message.chat.last_name}\n یوزرنیم شما : @{call.message.chat.username}\n ایدی عددی شما : {call.message.chat.id}")
    elif call.data == "he":
        bot.reply_to(call.message, f"سلام {call.message.chat.first_name} به بخش راهنمای ربات خوش آمدی 🤍 \n با کامند /start میتوانید ربات را استارت کنید و از قابلیت های ربات استفاده کنید \n پشتیبانی ربات : @V1TOW ")

bot.polling()
