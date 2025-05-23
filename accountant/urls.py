from django.urls import path
from . import views

urlpatterns = [
    path('accountantMain/', views.accountantMain, name='accountantMain'), 
    path('viewcars/', views.viewcars, name='viewcars'), 
    path('accountantWaybills/', views.accountantWaybills, name='accountantWaybills'), 
    path('create_waybills/', views.create_waybills, name='create_waybills'), 
    path('acc_drivers/', views.acc_drivers, name='acc_drivers'), 
    path('acc_expenses/', views.acc_expenses, name='acc_expenses'), 
        path('addExpenses/', views.addExpenses, name='addExpenses'),

]