from django.db import models

# Create your models here.

class UserData(models.Model):
    first_name = models.CharField(max_length=30)
    mname = models.CharField(max_length=30, null=True)
    lname = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)
    def __str__(self):
        return self.first_name


class Help(models.Model):
    Fname = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    Message = models.CharField(max_length=50)
