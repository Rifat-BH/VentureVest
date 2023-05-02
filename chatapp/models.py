from django.db import models
from auths.models import Auts
from datetime import datetime

class MessageDb(models.Model):
    s_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='s_id')
    r_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE, related_name='r_id')
    send_date = models.DateTimeField(default=datetime.now())
    msgg = models.CharField(max_length=1000)
    status = models.CharField(max_length=7, default ="unseen")

class MessageNofity(models.Model):
    msg_send_by = models.IntegerField()
    notify = models.CharField(max_length=50)
    user_id = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='user_id')
    status = models.IntegerField(default=0)
    comment_date = models.DateTimeField(default=datetime.now())


