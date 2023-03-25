from django.contrib import admin
from django.urls import path,include
from investor import views
urlpatterns = [
    path('', views.home, name="investor-home"),

]