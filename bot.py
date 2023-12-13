import telebot
from info import character_info
from config import token


bot = telebot.TeleBot(token)


photo_link = ('https://ya.ru/images/search?img_url=https%3A%2F%2Fwww.1zoom.ru%2Fbig2%2F706%2F253234-Sepik.jpg&lr'
              '=21647&pos=0&rpt=simage&source=serp&text=%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%20%D1%84%D0%BE%D1%82%D0%BE')


def filter_hello(message):
    text = 'привет'
    return text in message.text


def filter_bye(message):
    text = 'пока'
    return text in message.text


commands = {
        '1': 'Напишите /start чтобы бот заработал',
        '2': 'Напишите /help для вывода списка команд',
        '3': 'Напишите /info для получения визитки',
        '4': 'Напишите /cat если хотите чтобы бот прислал вам фото котика'}


#конец функций словарей импортов и переменных





@bot.message_handler(commands=['start'])
def handle_help(message):
    bot.send_message(message.chat.id,"Привет это бот-визитка\n"
                                     "Для того чтобы ознакомиться с командами введи /help")


@bot.message_handler(commands=['help'])
def get_menu(message):
    bot.send_message(message.chat.id, "\n".join(commands.values()))#как их склеить?


@bot.message_handler(commands=['info'])
def information_about_character(message):
    bot.send_message(message.chat.id,
                     f"Меня зовут {character_info['name']}, мне {character_info['age']} лет.\n"
                      f"Я очень {character_info['xobbi']}, а также иногда {character_info['interest']}.\n"
                      f"Я {character_info['education']}.\n"
                      f"Если хотите посмотреть мои проекты то вот ссылка на гитхаб {character_info['git']}")#шаблон


@bot.message_handler(commands=['cat'])
def cat_photo(message):
    bot.send_photo(message.chat.id, f'{photo_link}')#конец блока команд





@bot.message_handler(content_types=['text'], func = filter_hello)
def say_hello(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(content_types=['text'], func = filter_bye)
def say_goodbye(message):
    bot.send_message(message.chat.id, "До свидания!")


@bot.message_handler(content_types=['sticker'])
def sticker_answer(message):
      bot.send_message(message.chat.id, "Классный стикер, но все же используйте бота по назначению\n"
                                        "Введите /help")


@bot.message_handler(content_types=['text'])
def text_answer(message):
      bot.send_message(message.chat.id,
                       "Извините я вас не понял, пожалуйста введите команду или /help для просмотра списка команд")


@bot.message_handler(content_types=['audio','video','voice', 'photo'])
def media_answer(message):
      bot.send_message(message.chat.id, "К сожелению я всего лишь бот и не могу послушать и посмотреть все это\n"
                                        "Введите команду /help")


bot.polling()


