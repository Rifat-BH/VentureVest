from django.contrib import admin
from backupStartupDB.models import startupBasicInfo2, applyForFundrising, monthlyRevenue, profit

# Register your models here.
class startupAdmin2(admin.ModelAdmin):
    list_display=('user_id','companyName','companyAddress','companyDescription')
admin.site.register(startupBasicInfo2,startupAdmin2)

class startupApplyForFundrisingAdmin(admin.ModelAdmin):
    list_display=('user_id','name','duration','investment','Repayments','description','image','vat','bin','licence','revenue','gross_margin','mrr','cac','burn_rate','status')
admin.site.register(applyForFundrising,startupApplyForFundrisingAdmin)

class monthlyRevenueAdmin(admin.ModelAdmin):
    list_display=('user_id','month','currentRevenue','currentProfit')
admin.site.register(monthlyRevenue,monthlyRevenueAdmin)

class ProfitAdmin(admin.ModelAdmin):
    list_display=('st_id','ammount','inv_id','comments', 'date')
admin.site.register(profit,ProfitAdmin)