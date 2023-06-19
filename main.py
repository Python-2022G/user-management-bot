from flask import Flask, request
import requests

bot_app = Flask(__name__)
TOKEN = '6025180683:AAEEPoYUMu35d_m5ZtyMv03XUcgr0TzOfRM'


@bot_app.route('/webhook/', methods=['POST', 'GET'])
def webhook_bot():
    if request.method == 'GET':
        return "Webhook is working now!"
    
    elif request.method == "POST":
        update = request.get_json()

        chat_id = update['message']['chat']['id']
        text    = update['message']['text']

        payload = {
            'chat_id': chat_id,
            'text': text
        }

        print(update, '\n\n')
        print(chat_id, text, '\n\n', '\n\n', '\n\n')


        requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=payload)

        return 'ok'