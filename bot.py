from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from callbakcs import (
    start,
)

TOKEN = '6025180683:AAEEPoYUMu35d_m5ZtyMv03XUcgr0TzOfRM'

def main():
    udpater = Updater(TOKEN)

    dp = udpater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    udpater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()
