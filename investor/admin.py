from django.contrib import admin
from investor.models import Invest

class InvestAdmin(admin.ModelAdmin):
        list_display = ('user_id', 'date', 'company_name')

# Register your models here.
admin.site.register(Invest,InvestAdmin)
