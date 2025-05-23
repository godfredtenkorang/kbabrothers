from django.shortcuts import render

def accountantMain(request):
    return render(request, 'accountant/accountantMain.html')

def viewcars(request):
    return render(request, 'accountant/viewcars.html')
 

def accountantWaybills(request):
    return render(request, 'accountant/accountantWaybills.html')
 

def create_waybills(request):
    return render(request, 'accountant/create_waybills.html')
 

def acc_drivers(request):
    return render(request, 'accountant/acc_drivers.html')
 

def acc_expenses(request):
    return render(request, 'accountant/acc_expenses.html')


def addExpenses(request):
    return render(request, 'accountant/addExpenses.html')

 