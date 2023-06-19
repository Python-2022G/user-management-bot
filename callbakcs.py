from telegram import Update
from telegram.ext import CallbackContext
import requests

URL = 'http://rramazonov.pythonanywhere.com'


def start(udpate: Update, context: CallbackContext):
    user = udpate.effective_user

    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "chat_id": user.id
    }

    response = requests.post(f'{URL}/users', json=data)

    if response.status_code == 200:
        udpate.message.reply_html(f'Hello <b>{user.first_name}</b>!\n\nWelcome to our registration bot! <i>You\'ve just registred.</i>')
    else:
        udpate.message.reply_html(f'Hi <b>{user.first_name}</b>!\n\nWelcome to our registration bot! <i>You\'ve already been registred.</i>')
