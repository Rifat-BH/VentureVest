from django.contrib import admin
from blogs.models import blogs

# Register your models here.
class startupAdmin(admin.ModelAdmin):
    list_display=('user_id','name','title','description','date','image')
admin.site.register(blogs,startupAdmin)