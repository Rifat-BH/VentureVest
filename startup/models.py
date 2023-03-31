from django.db import models
from auths.models import Auts

# Create your models here.
class startupBasicInfo(models.Model):
    user_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE)
    name = models.CharField (max_length=100)
    duration = models.IntegerField()
    investment = models.IntegerField()
    roi = models.IntegerField()
    Repayments = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default="")
    vat = models.ImageField(default="")
    bin = models.ImageField(default="")
    licence = models.ImageField(default="")
