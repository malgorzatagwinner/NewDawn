from django.contrib import admin
from .models import Document
from django.contrib.auth.admin import UserAdmin
#from .models import User
# Register your models here.
from django.contrib.auth.models import User

admin.site.register(Document)
#admin.site.register(User, UserAdmin)
