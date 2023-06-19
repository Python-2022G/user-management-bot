from telegram import Bot
from bot import TOKEN


bot = Bot(TOKEN)

def get_info():
    print(bot.get_webhook_info())

def delete_webhook():
    print(bot.delete_webhook())  

def set_webhook(url):
    print(bot.set_webhook(url=url))

# set_webhook('https://google.com/webhook/')
# get_info()