from django.contrib import admin
from chatapp.models import MessageDb, MessageNofity
# Register your models here.
class MessageDbAdmin(admin.ModelAdmin):
    list_display = ('s_id','r_id', 'send_date', 'msgg', 'status')
class MessageNotfAdmin(admin.ModelAdmin):
    list_display = ('msg_send_by','notify', 'user_id', 'status', 'comment_date')
admin.site.register(MessageDb,MessageDbAdmin)
admin.site.register(MessageNofity,MessageNotfAdmin)
