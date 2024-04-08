import requests
import json

from django.conf import settings

bot_token = settings.TELEGRAM_BOT_API


def send_message(user_id):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
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
