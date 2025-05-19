from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addvehicles/', views.addvehicles, name='addvehicles'),
    path('view_Vehicles/', views.view_Vehicles, name='view_Vehicles'),
    path('drivers/', views.drivers, name='drivers'),
    path('expenses/', views.expenses, name='expenses'),
    path('waybills/', views.waybills, name='waybills'),
    path('createwayBills/', views.createwayBills, name='createwayBills'),
    path('addExpenses/', views.addExpenses, name='addExpenses'),
]