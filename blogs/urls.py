from django.contrib import admin
from django.urls import path,include
from blogs import views

urlpatterns = [
    path('blogDetails/', views.blogDetails, name="blogDetails"),
    path('blogList/', views.blogList, name="blogList"),
    path('blogPost/', views.blogPost, name="blogPost"),
]