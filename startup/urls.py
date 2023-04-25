from django.contrib import admin
from django.urls import path,include
from startup import views

urlpatterns = [
    path('home/', views.startupInfo, name="startupHome"),
    path('startupBasicInfo/', views.startupInfo, name="startupBasicInfo"),
    path('startupDetails/<id>', views.startupDetailsViews, name="startupDetails"),
    path('startupDashboard/', views.startupDashboard, name="startupDashboard"),
    path('applyForFundrising/', views.applyForFundrisingViews, name="applyForFundrising"),
    path('monthlyRevenue/', views.monthlyRevenueViews, name="monthlyRevenue"),
    path('startupList/', views.startupList, name="startupList"),
]