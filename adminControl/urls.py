from django.contrib import admin
from django.urls import path,include
from adminControl import views

urlpatterns = [
    path('home/', views.adminApproval, name="adminApproval"),
    path('adminControl/', views.adminApproval, name="adminApproval"),
    
]