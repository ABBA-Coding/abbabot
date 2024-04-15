import requests
import json

import os
from bazaapp.models import TelegramGroups, Projects, Status

from django.conf import settings

bot_token = settings.TELEGRAM_BOT_API
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
GROUP_ID = settings.GROUP_ID

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bazasite.settings')



def send_message(user_id):
    keyboard = {
        "inline_keyboard": [
            [{"text": "Abbaweb", "web_app": {"url": settings.BASE_URL}}],
        ]
    }
    reply_markup = json.dumps(keyboard)
    message_text = 'Ushbu havola orqali kiring:'
    payload = {
        'chat_id': user_id,
        'text': message_text,
        'reply_markup': reply_markup
    }
    requests.post(url, json=payload)


def periodic_send_message():
    for i in TelegramGroups.objects.all():
        try:
            for project in Projects.objects.all():
                for status in Status.objects.all():
                    message_text = (f'Proyekt nomi: {project.title}'
                                    f'Jarayoni: {status.title}'
                                    f'Proyekt Vaqti: {project.created_at}')
                    payload = {
                        'chat_id': i.group.id,
                        'text': message_text
                    }
                    requests.post(url, json=payload)
        except:
            print("Guruh id ishlamayabdi")



def send_notification(text):
    print("HHHHH")
    payload = {
        'chat_id': GROUP_ID,
        'text': text
    }
    requests.post(url, json=payload)
