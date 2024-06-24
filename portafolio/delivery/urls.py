from django.urls import path
from . import views

urlpatterns = [
    path('newshipment/', views.new_shipment, name='newshipment'),
    path('searchshipment/', views.search_shipment, name='searchshipment'),
    path('myshipments/', views.my_shipments, name='myshipments'),
    path('sendmoney/', views.send_money, name='sendmoney'),
]
