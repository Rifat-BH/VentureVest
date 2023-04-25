from django.contrib import admin
from backupStartupDB.models import startupBasicInfo2

# Register your models here.
class startupAdmin2(admin.ModelAdmin):
    list_display=('user_id','companyName','companyAddress','companyDescription')
admin.site.register(startupBasicInfo2,startupAdmin2)