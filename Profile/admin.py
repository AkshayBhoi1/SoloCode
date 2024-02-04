from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(UserData)
class UserDetails(admin.ModelAdmin):
    list_display = ['first_name', 'mname', 'lname', 'contact', 'email', 'address', 'city', 'state', 'zip']


@admin.register(Help)
class UserDetails(admin.ModelAdmin):
    list_display = ['Fname', 'email', 'contact', 'Message']