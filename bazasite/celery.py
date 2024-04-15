import os

from celery.schedules import crontab
from celery import Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bazasite.settings")
app = Celery('bazasite')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'daily-function': {
        'task': 'bot.functions.periodic_send_message',
        'schedule': crontab(hour=7),
    }
}
