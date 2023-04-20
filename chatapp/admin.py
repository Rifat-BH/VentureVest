from django.contrib import admin
from chatapp.models import MessageDb
# Register your models here.
class MessageDbAdmin(admin.ModelAdmin):
    list_display = ('s_id','r_id', 'send_date', 'msgg')
admin.site.register(MessageDb,MessageDbAdmin)
