from django.db import models
from auths.models import Auts
from datetime import datetime


# Create your models here.
class blogs(models.Model):
    user_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE)
    name = models.CharField (max_length=100)
    title = models.CharField (max_length=100)
    description = models.CharField (max_length=5000)
    image = models.ImageField(default="")
    date = models.DateTimeField(default=datetime.now())