from django.db import models

# Create your models here.
class certificate(models.Model):
    file = models.FileField()

class Quiz(models.Model):
    ans = models.CharField(max_length=120)
    sub = models.CharField(max_length=10)

class CQuiz(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    def __str__(self):
        return self.Question

class CppQuiz(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    def __str__(self):
        return self.Question


class JavaQuiz(models.Model):
    Question = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    def __str__(self):
        return self.Question


class JsQuiz(models.Model):
    Question = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    def __str__(self):
        return self.Question


class PhpQuiz(models.Model):
    Question = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    def __str__(self):
        return self.Question


class PythonQuiz(models.Model):
    Question = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    def __str__(self):
        return self.Question


class Caccess(models.Model):
    number = models.IntegerField(max_length=1)


class Cppaccess(models.Model):
    number = models.IntegerField(max_length=1)


class Pythonaccess(models.Model):
    number = models.IntegerField(max_length=1)


class Javaacces(models.Model):
    number = models.IntegerField(max_length=1)


class Jsaccess(models.Model):
    number = models.IntegerField(max_length=1)


class Phpaccess(models.Model):
    number = models.IntegerField(max_length=1)
