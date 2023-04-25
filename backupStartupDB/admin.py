from django.contrib import admin
from backupStartupDB.models import startupBasicInfo2, applyForFundrising

# Register your models here.
class startupAdmin2(admin.ModelAdmin):
    list_display=('user_id','companyName','companyAddress','companyDescription')
admin.site.register(startupBasicInfo2,startupAdmin2)

class startupApplyForFundrisingAdmin(admin.ModelAdmin):
    list_display=('user_id','name','duration','investment','Repayments','description','image','vat','bin','licence','revenue','gross_margin','mrr','cac','burn_rate')
admin.site.register(applyForFundrising,startupApplyForFundrisingAdmin)