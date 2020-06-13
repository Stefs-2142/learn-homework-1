"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import settings
import logging
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Расширенное логирование, с датой и временем.
logging.basicConfig(filename='bot.log', level=logging.INFO,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    text = 'Вызван /start'
    update.message.reply_text(text)

def get_ephem_info(update, context):
    """Определяет в каком  совездии сегодня находится объект"""

    entered_planet = update.message.text.split()[-1].capitalize()  # Получаем название планеты из пользовательского ввода команды /planet {planet_name}
    if hasattr(ephem, entered_planet):                             # Проверяем есть ли введённая планета
        planet = getattr(ephem, entered_planet)
        
        today = datetime.today()
        planet_loc = ephem.constellation(planet(today))    # Запрашиваем локацию на сегодняшний день
        formated_planet_loc = (f'{entered_planet} is in the constellation: {planet_loc[-1]}')
        update.message.reply_text(formated_planet_loc)
    else:
        update.message.reply_text('Whoops try again')    

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def wordcounter(update, context):
    """Определяет количество введёных слов"""
    
    words_for_count = update.message.text.split()[1:] 
    if len(words_for_count) >= 1 and update.message.text[10:].replace(' ', '').isalpha(): # Проверка на пустое сообщение и проверка на введение чисел.
        if len(words_for_count) == 1:
            update.message.reply_text(f'{len(words_for_count)} слово.')
        elif len(words_for_count) <= 4:
            update.message.reply_text(f'{len(words_for_count)} слова.')
        else:
            update.message.reply_text(f'{len(words_for_count)} слов.')
    else:
        update.message.reply_text('Попробуйте ввести слова.')
    
    
    
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_ephem_info))
    dp.add_handler(CommandHandler("wordcount", wordcounter))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

