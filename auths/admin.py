from django.contrib import admin
from auths.models import Auts
class Authsadmin(admin.ModelAdmin):
    list_display=('user_name', 'password','catagory', 'full_name', 'email')
admin.site.register(Auts,Authsadmin)
# Register your models here.
