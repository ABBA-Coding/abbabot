from celery.schedules import crontab
from celery import Celery

app = Celery('bazasite')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule ={
    'daily-function': {
        'task': 'bot.function.periodic_send_message',
        'schedule': crontab(hour='07', minute='00'),
    }
}
