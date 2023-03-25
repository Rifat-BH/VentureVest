from django.contrib import admin
from django.urls import path,include
from auths import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
]
