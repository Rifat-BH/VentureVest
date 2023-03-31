from django.contrib import admin
from django.urls import path,include
from auths import views

urlpatterns = [
    path('', views.login, name="login"),
<<<<<<< HEAD
=======
    path('login/', views.login, name="login"),
>>>>>>> startup
    path('signup/', views.signup, name="signup"),
    path('signout/', views.logout, name="logout"),
]
