import requests
import json
from celery import Celery
from celery.schedules import crontab
import os

from django.conf import settings

bot_token = settings.TELEGRAM_BOT_API
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
GROUP_ID = settings.GROUP_ID

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bazasite.settings')
app = Celery('bazasite')


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


def periodic_send_message(user_id):
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

app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule ={
    'daily-function': {
        'task': 'bot.function.periodic_send_message',
        'schedule': crontab(hour='16', minute='00'),
    }
}


def send_notification(text):
    print("HHHHH")
    payload = {
        'chat_id': GROUP_ID,
        'text': text
    }
    requests.post(url, json=payload)
