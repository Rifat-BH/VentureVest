from django.contrib import admin
from django.urls import path,include
from auths import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.logout, name="logout"),
    path('otp/', views.otp_view, name="otp"),
    path('hijack/', include('hijack.urls')),
]
