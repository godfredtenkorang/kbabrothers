from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mysite/index.html')

def addvehicles(request):
    return render(request, 'mysite/vehicles.html')

def view_Vehicles(request):
    return render(request, 'mysite/view_Vehicles.html')


def drivers(request):
    return render(request, 'mysite/drivers.html')

def expenses(request):
    return render(request, 'mysite/expenses.html')

def waybills(request):
    return render(request, 'mysite/waybills.html')

def createwayBills(request):
    return render(request, 'mysite/createwayBills.html')

def report(request):
    return render(request, 'mysite/report.html')