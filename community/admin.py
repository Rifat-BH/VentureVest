from django.contrib import admin
from community.models import CommunityPost,CommunityComment,CommentNofity
class CommunityPostdmin(admin.ModelAdmin):
    list_display = ('post_by', 'post_date', 'post_title', 'post_des')

class CommunityCommentAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'comment_by', 'comment', 'comment_date')
class CommentNotifyAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'comment_by', 'notify', 'post_by', 'status', 'comment_date')
# Register your models here.
admin.site.register(CommunityPost,CommunityPostdmin)
admin.site.register(CommunityComment,CommunityCommentAdmin)
admin.site.register(CommentNofity,CommentNotifyAdmin)