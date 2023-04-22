from django.db import models
from auths.models import Auts
from datetime import datetime
# Create your models here.

class CommunityPost(models.Model):
    post_by = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='post_by')
    post_date = models.DateTimeField(default=datetime.now())
    post_title = models.CharField(max_length=50)
    post_des = models.CharField(max_length=1000)

class CommunityComment(models.Model):
    post_id = models.ForeignKey(CommunityPost,blank = True, null = True, on_delete= models.CASCADE,related_name='post_id')
    comment_by = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='comment_by')
    comment = models.CharField(max_length=500)
    comment_date = models.DateTimeField(default=datetime.now())

class CommentNofity(models.Model):
    post_id = models.IntegerField()
    comment_by = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='nf_comment_by')
    notify = models.CharField(max_length=30)
    post_by = models.ForeignKey(Auts,blank = True, null = True, on_delete= models.CASCADE,related_name='nf_post_by')
    status = models.IntegerField(default=0)
    comment_date = models.DateTimeField(default=datetime.now())