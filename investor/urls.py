from django.contrib import admin
from django.urls import path,include
from investor import views
urlpatterns = [
    path('home/', views.home, name="investor-home"),

]