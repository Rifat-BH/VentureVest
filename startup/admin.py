from django.contrib import admin

# Register your models here.
from startup.models import startupBasicInfo

class startupAdmin(admin.ModelAdmin):
    list_display=('name','duration','investment','Repayments','description','image','vat','bin','licence')
admin.site.register(startupBasicInfo,startupAdmin)