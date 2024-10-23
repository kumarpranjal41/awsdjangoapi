from django.db import models

# Create your models here.

class signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    dep= models.CharField(max_length=20 , choices= (('IT' , 'IT') , ('NON-IT' , 'NON-IT')))
