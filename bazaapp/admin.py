from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Projects)
admin.site.register(Status)
admin.site.register(HeadCategory)
admin.site.register(TelegramGroups)


