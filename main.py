import telebot
from telebot import types
import re
import datetime
from ImageParser import YandexImage
token = "2057968380:AAH9PVMhZR76QD_FYJxJ9x9Wy_LPxkzde_k"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'привет, хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    s = 'Команды и ответы \n /start - начать общение \n /help - список команд \n /calculator - арифметические операции с двумя натуральными числами \n /newyear - сколько времени до Нового года \n /search - картинка по данному запросу \n как дела? \n в чём смысл жизни? \n идущий к реке '
    bot.send_message(message.chat.id, s)


@bot.message_handler(commands=['calculator'])
def calculator(message):
    a = message.text.split('/calculator ')[1]
    a = ''.join([x for x in a if x != ' '])
    znak = ''.join([x for x in a if not x.isdigit()])
    x, y = map(int, re.split("\+|\-|\/|\*", a))
    if znak == '+':
        res = x + y
    elif znak == '-':
        res = x - y
    elif znak == '*':
        res = x * y
    elif znak == '/':
        res = x / y
    else:
        res = 'Неопознанный оператор'
    bot.send_message(message.chat.id, res)


@bot.message_handler(commands=['newyear'])
def ny(message):
    now = datetime.datetime.today()
    NY = datetime.datetime(2022, 1, 1)

    d = NY - now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)

    res = f'До Нового года осталось {d.days} дней, {hh} часов, {mm} минут и {ss} секунд'
    bot.send_message(message.chat.id, res)


@bot.message_handler(commands=['search'])
def searchimg(message):
    a = message.text.split('/search ')[1].lower()
    parser = YandexImage()
    url = parser.search(a)[0].url
    bot.send_photo(message.chat.id, url)





@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, 'У создателя бота отлично, надеюсь, у тебя тоже!')
    elif message.text.lower() == "в чём смысл жизни?":
        bot.send_message(message.chat.id, 'Задавать вопросы без ответа')
    elif message.text.lower() == "идущий к реке":
        s = 'Я в своем познании настолько преисполнился, что я как будто бы уже сто триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет, как эта Земля, мне этот мир абсолютно понятен, и я здесь ищу только одного - покоя, умиротворения и вот этой гармонии, от слияния с бесконечно вечным, от созерцания великого фрактального подобия и от вот этого замечательного всеединства существа, бесконечно вечного, куда ни посмотри, хоть вглубь - бесконечно малое, хоть ввысь - бесконечное большое, понимаешь?'
        bot.send_message(message.chat.id, s)
    else:
        bot.send_message(message.chat.id, 'Не знаю, что тебе ответить')

if __name__ == '__main__':
    bot.infinity_polling()