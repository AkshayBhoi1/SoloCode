from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(CQuiz)
class cdetails(admin.ModelAdmin):
    list_display = ['Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Corrans']


@admin.register(CppQuiz)
class cppdetails(admin.ModelAdmin):
    list_display = ['Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Corrans']


@admin.register(JavaQuiz)
class javadetails(admin.ModelAdmin):
    list_display = ['Question', 'Corrans']


@admin.register(JsQuiz)
class jsdetails(admin.ModelAdmin):
    list_display = ['Question', 'Corrans']


@admin.register(PhpQuiz)
class phpdetails(admin.ModelAdmin):
    list_display = ['Question', 'Corrans']


@admin.register(PythonQuiz)
class pydetails(admin.ModelAdmin):
    list_display = ['Question', 'Corrans']

@admin.register(Quiz)
class an(admin.ModelAdmin):
    list_display = ['ans', 'sub']

@admin.register(Caccess)
class access1(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Cppaccess)
class access2(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Pythonaccess)
class access3(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Jsaccess)
class access4(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Javaacces)
class access5(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Phpaccess)
class access6(admin.ModelAdmin):
    list_display = ['number']


@admin.register(certificate)
class certi(admin.ModelAdmin):
    list_display = ['file']