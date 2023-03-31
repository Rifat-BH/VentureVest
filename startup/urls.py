from django.contrib import admin
from django.urls import path,include
from startup import views

urlpatterns = [
    path('startupBasicInfo/', views.startupInfo, name="startupBasicInfo"),
    path('startupDashboard/', views.startupDashboard, name="startupDashboard"),
]