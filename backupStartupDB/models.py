from django.db import models
from auths.models import Auts

# Create your models here.

class startupBasicInfo2(models.Model):
    user_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE)
    companyName = models.CharField (max_length=100,default="")
    companyAddress = models.CharField (max_length=100,default="")
    companyDescription = models.CharField (max_length=500,default="")