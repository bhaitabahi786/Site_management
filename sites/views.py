from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def sites(request):
    return render(request,'sites/sitepage.html')

def addSites(request):
    return render(request,'sites/AddSitePage.html')

def ManageSites(request):
    return render(request,'sites/ManageSitePage.html')

def AddManpower(request):
    return render(request,'sites/AddManpowerPage.html')

def AddExpenses(request):
    return render(request,'sites/AddExpensesPage.html')

def AddTools(request):
    return render(request,'sites/AddToolsPage.html')

def LabourDetails(request):
    return render(request,'sites/LabourDetails.html')




