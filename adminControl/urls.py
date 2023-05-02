from django.contrib import admin
from django.urls import path,include
from adminControl import views

urlpatterns = [
    path('home/', views.adminDetails, name="adminDetails"),
    path('adminControl/', views.adminDetails, name="adminDetails"),
    path('adminApproval/<id>', views.adminApproval, name="adminApproval"),
    path('adminDeny/<id>', views.adminDeny, name="adminDeny"),

]