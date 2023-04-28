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
    path('fundingList/', views.funding_details, name="funding"),
    path('return-profit/', views.return_profit, name="return-profit"),
    path('return-profit-db/', views.return_profit_save_db, name="returnProfit"),
   
]