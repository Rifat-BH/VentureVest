from django.db import models

# Create your models here.
class Auts(models.Model):
    user_name = models.CharField(max_length=35)
    password = models.CharField(max_length=128)
    catagory = models.CharField(max_length=10)
    full_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=35)
    