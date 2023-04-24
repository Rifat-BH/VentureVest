from django.db import models
from auths.models import Auts

# Create your models here.
class Invest(models.Model):
    user_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE)
    date = models.DateField()
    company_name = models.CharField(max_length=50)
    invest_ammount = models.CharField(max_length=10)
    returen_rate = models.CharField(max_length=5)
    
    
# auto_now_add=True