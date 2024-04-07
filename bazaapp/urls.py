from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', project_by_category, name='projects'),
    path('headcategory/<int:headcategory_id>/', head_by_category, name='headcategory'),
    path('projectspage', projectpage, name='projectpage'),
    path('statuspage', statuspage, name='statuspage'),
    path('sendmessage', send_message, name='sendmessage'),
]
