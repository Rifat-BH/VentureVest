from django.contrib import admin
from django.urls import path,include
from investor import views
urlpatterns = [
    path('home/', views.home, name="investor-home"),
    path('home/get_tabledata/', views.get_data_table, name="investor-home"),
    path('home/get_graph1data/', views.get_data_graph1, name="investor-home"),
    path('home/post_invest_data/', views.investData, name="invest"),
    path('company_rev_details/<cname>', views.get_data_graph2, name="see_details"),
    path('company_rev_details-ajax/<cid>', views.get_data_graph2_ajax, name="see_details_ajax"),
    path('payment/', views.payment, name="payment-gateway"),
    path('profit-table/', views.profit_table, name="profit-table"),
]