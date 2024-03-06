from django.shortcuts import render, get_object_or_404,redirect
from .models import *

# Create your views here.

from django.http import HttpResponse

def sites(request):
    sites = Site.objects.all()
    return render(request, 'sites/sitepage.html', {'sites': sites})

def addSites(request):

    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        site_address = request.POST.get('site_address')
        quotation_amount = request.POST.get('quotation_amount')
        
        SiteAdd = Site(name=site_name, address=site_address, quotation_amount=quotation_amount)
        SiteAdd.save()
        return redirect('sites')

    return render(request,'sites/AddSitePage.html')

def ManageSites(request,site_id):
    siteInfo = get_object_or_404(Site, pk=site_id)

    manpowers = Manpower.objects.all()

    return render(request,'sites/ManageSitePage.html',{'siteInfo':siteInfo,'manpowers':manpowers})

def AddManpower(request,site_id):
    siteInfo = get_object_or_404(Site, pk=site_id)

    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        site_name2 = Site.objects.get(name=site_name)
        emp_name = request.POST.get('emp_name')
        aadhar_no = request.POST.get('aadhar_no')
        contact = request.POST.get('contact')
        
        ManpowerAdd = Manpower(site=site_name2, name=emp_name, adhaarno=aadhar_no, contact=contact)
        ManpowerAdd.save()
        return redirect('ManageSites',site_id=site_id)

    return render(request,'sites/AddManpowerPage.html',{'siteInfo':siteInfo})

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

def delete_Manpower(request, man_id, site_id):
    manpower = get_object_or_404(Manpower, pk=man_id)
    manpower.delete()
    return redirect('ManageSites',site_id=site_id)


