from django.contrib import admin
from django.urls import path,include
from chatapp import views
urlpatterns = [
    path('startup/', views.home, name="investor-home"),
    path('startup-profile/<rec_id>', views.get_message, name="get_mag"),
    path('startup-profilemsg/<rec_id>', views.get_messages, name="get_mag"),
    path('startup/send', views.send_message, name="send_mag"),


]