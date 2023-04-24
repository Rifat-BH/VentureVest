from django.contrib import admin
from django.urls import path,include
from investor import views
urlpatterns = [
    path('home/', views.home, name="investor-home"),
    path('home/get_tabledata/', views.get_data_table, name="investor-home"),
    path('home/get_graph1data/', views.get_data_graph1, name="investor-home"),
    path('home/post_invest_data/', views.investData, name="invest"),

]