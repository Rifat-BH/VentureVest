from django.contrib import admin
from django.urls import path,include
from startup import views

urlpatterns = [
    path('home/', views.startupInfo, name="startupHome"),
    path('startupBasicInfo/', views.startupInfo, name="startupBasicInfo"),
    path('startupDashboard/', views.startupDashboard, name="startupDashboard"),
    path('startup-Details/<st_id>', views.startupDetails, name="startup-Details"),
    path('startupList/', views.startupList, name="startupList"),
]