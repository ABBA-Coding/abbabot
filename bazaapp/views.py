from django.shortcuts import render
from .models import *
from bot.functions import send_notification


def index(request):
    categories = Category.objects.all()
    headcategories = HeadCategory.objects.all()
    context = {
        'title': "AbbaWeb",
        'categories': categories,
        'headcategories': headcategories

    }

    return render(request, 'bazaapp/index.html', context)


def projectpage(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
        'title': "AbbaWeb"
    }

    return render(request, "bazaapp/projectpage.html", context)


def statuspage(request, product_id):
    status = Status.objects.all()[:12]
    leftstatus = Status.objects.all()[12:]
    context = {
        'status': status,
        'leftstatus': leftstatus,
        'title': "ABBAWeb",
        'product_id': product_id
    }

    return render(request, "bazaapp/statuspage.html", context)


def project_by_category(request, category_id):
    project = Projects.objects.filter(category__id=category_id)
    context = {
        'categories': Category.objects.all(),
        'projects': project,
    }
    return render(request, 'bazaapp/projectpage.html', context)


def head_by_category(request, headcategory_id):
    categories = Category.objects.filter(headcategory_id=headcategory_id)
    context = {
        'categories': categories,
    }
    return render(request, 'bazaapp/categorypage.html', context)


def send_message(request, product_id, status_id):
    project = Projects.objects.get(pk=product_id)
    status = Status.objects.get(pk=status_id)
    text = (f"Proyekt nomi: {project.title}\n"
        f"Jarayoni: {status.title}\n"
        f"Boshlangan vaqti: {project.get_day()}\n"
        f"Jarayonlar vaqti: {project.deadline_time}")
    send_notification(text, project.group.group_id)
    return render(request, 'bazaapp/succeessfulmessage.html')


import requests
from django.conf import settings
from django.http import HttpResponse

bot_token = settings.TELEGRAM_BOT_API
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
GROUP_ID = settings.GROUP_ID


def periodic_send_message(request):
    for i in TelegramGroups.objects.all():
        try:
            for project in Projects.objects.all():
                message_text = (f'Proyekt nomi: {project.title}\n',
                                f'Jarayoni: {project.status.title}\n'
                                f'Proyekt Vaqti: {project.created_at}')
                payload = {
                    'chat_id': i.group_id,
                    'text': message_text
                }
                requests.post(url, json=payload)
        except:
            print("Guruh id ishlamayabdi")
    return HttpResponse('ok')
