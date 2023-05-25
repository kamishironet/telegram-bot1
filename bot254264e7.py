import telebot
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"hi niga")


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id,"Привет, ты говоришь с ботом")
    elif message.text == "/help":
        bot.send_message(message.from_user.id,"Напиши ,привет,что бы получить больше информации")
    else:
        bot.send_message(message.from_user.id,"я тебя не понимаю")
name=''
age = 0
surname=''
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id,"Как тебя зовут?")
        bot.register_next_step_handler(message,get_name)
def get_name(message):
    global name 
    name = message.text
    bot.send_message(message.from_user.id,"какая у тебя фамилия?")
    bot.register_next_step_handler(message,get_surname)







bot.polling(none_stop = True)
    