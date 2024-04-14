from .celery import app as celery_app
import os

__all__ = ('celery_app',)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bazasite.settings')
