from django.contrib import admin
from .models import Document
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(Document)
admin.site.register(User, UserAdmin)
