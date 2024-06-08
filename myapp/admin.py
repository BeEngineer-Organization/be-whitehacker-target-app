from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, TalkRoom, Message

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(TalkRoom)
admin.site.register(Message)
