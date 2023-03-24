from django.contrib import admin
from django.urls import path,include
from auths import views

urlpatterns = [
    path('', views.login, name="login"),
]
