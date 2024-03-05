from django.shortcuts import render, get_object_or_404,redirect
from .models import Site

# Create your views here.

from django.http import HttpResponse

def sites(request):
    sites = Site.objects.all()
    return render(request, 'sites/sitepage.html', {'sites': sites})

def addSites(request):
    return render(request,'sites/AddSitePage.html')

def ManageSites(request,site_id):
    siteInfo = get_object_or_404(Site, pk=site_id)
    print(siteInfo)

    return render(request,'sites/ManageSitePage.html',{'siteInfo':siteInfo})

def AddManpower(request):
    return render(request,'sites/AddManpowerPage.html')

def AddExpenses(request):
    return render(request,'sites/AddExpensesPage.html')

def AddTools(request):
    return render(request,'sites/AddToolsPage.html')

def LabourDetails(request):
    return render(request,'sites/LabourDetails.html')

def delete_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    site.delete()
    return redirect('sites')


