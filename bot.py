import logging
from pprint import pprint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL, 
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван /start")


    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

    # print(update)

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "*__main__":
    main()
