from django.db import models

# Create your models here.
class startupBasicInfo(models.Model):
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
