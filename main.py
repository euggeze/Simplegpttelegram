import g4f
import telebot
from telebot import types

bot = telebot.TeleBot('6779749096:AAEEL9TwxECbu2oKgjvIbUJVmjo9eAPPO5g')
model = "gpt-3.5-turbo"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Hello. I'm Kelas. You can asking me) \nIf you want to change model call /change_model")


@bot.message_handler(commands=['change_model'])
def change_model(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/set gpt-3.5-turbo-16k')
    btn2 = types.KeyboardButton('/set gpt-4-0613')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Bro, you can choose your preferred model)", reply_markup=markup)


@bot.message_handler(commands=['set'])
def set_model(message):
    global model
    model = message.text.split('/set ', 1)[1]

    bot.send_message(message.from_user.id, f"Ok, right now I have {model} brain)")



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    response = g4f.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": message.text}],
        stream=False,
    )
    bot.send_message(message.from_user.id, response)

bot.polling(none_stop=True, interval=0)