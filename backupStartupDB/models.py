from django.db import models
from auths.models import Auts
from datetime import date
# Create your models here.

class startupBasicInfo2(models.Model):
    user_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE)
    companyName = models.CharField (max_length=100,default="")
    companyAddress = models.CharField (max_length=100,default="")
    companyDescription = models.CharField (max_length=500,default="")
    
class applyForFundrising(models.Model):
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
    revenue = models.IntegerField()
    gross_margin = models.IntegerField()
    mrr = models.IntegerField()
    cac = models.IntegerField()
    burn_rate = models.IntegerField()
    status = models.IntegerField(default=0)
    
class monthlyRevenue(models.Model):
    user_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE)
    month = models.DateTimeField()
    currentRevenue = models.IntegerField()
    currentProfit = models.IntegerField()

class profit(models.Model):
    st_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='st_id')
    ammount = models.IntegerField()
    inv_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='inv_id')
    date = models.DateField(default=date.today)
    comments = models.CharField(max_length=30)
    # st_id = models.IntegerField()
    # inv_id = models.IntegerField()