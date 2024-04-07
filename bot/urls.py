from django.urls import path
from .views import *

urlpatterns = [
    path('', telegram_webhook, name='bot'),
]
