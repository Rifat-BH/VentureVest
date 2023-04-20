from django.db import models
from auths.models import Auts
from datetime import datetime

class MessageDb(models.Model):
    s_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='s_id')
    r_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE, related_name='r_id')
    send_date = models.DateTimeField(default=datetime.now())
    msgg = models.CharField(max_length=1000)


