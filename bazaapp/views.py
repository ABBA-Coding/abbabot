from django.shortcuts import render
from django.views.generic import ListView
from pprint import pprint
from .models import *


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


def statuspage(request):
    status = Status.objects.all()[:12]
    leftstatus = Status.objects.all()[12:]
    context = {
        'status': status,
        'leftstatus': leftstatus,
        'title': "ABBAWeb"
    }

    return render(request, "bazaapp/statuspage.html", context)


def project_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    project = Projects.objects.filter(category__id=category_id)
    context = {
        'categories': Category.objects.all(),
        'projects': project,
        'title': category.title
    }
    return render(request, 'bazaapp/projectpage.html', context)


def head_by_category(request, headcategory_id):
    categories = Category.objects.filter(headcategory_id=headcategory_id)
    context = {
        'headcategories': HeadCategory.objects.all(),
        'categories': categories,
        'title': categories[0].title
    }
    print(context['categories'])
    return render(request, 'bazaapp/categorypage.html', context)



def send_message(request):
    return render(request, 'bazaapp/succeessfulmessage.html')
