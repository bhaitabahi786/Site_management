from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from datetime import datetime
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
    expenses = Expense.objects.all()
    Tools = Tool.objects.all()

    return render(request,'sites/ManageSitePage.html',{'siteInfo':siteInfo,'manpowers':manpowers,'expenses':expenses,'Tools':Tools})

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

def AddExpenses(request,site_id):
    
    siteInfo = get_object_or_404(Site, pk=site_id)

    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        site_name2 = Site.objects.get(name=site_name)
        date_str = request.POST.get('date')
        # Convert the date to YYYY-MM-DD format
        date = datetime.strptime(date_str, '%b %d, %Y').strftime('%Y-%m-%d')
        expense_type = request.POST.get('expense_type')
        amount = request.POST.get('amount')
        
        ExpenseAdd = Expense(site=site_name2, date=date, description=expense_type, amount=amount)
        ExpenseAdd.save()
        return redirect('ManageSites',site_id=site_id)

    return render(request,'sites/AddExpensesPage.html',{'siteInfo':siteInfo})

def AddTools(request,site_id):

    siteInfo = get_object_or_404(Site, pk=site_id)

    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        site_name2 = Site.objects.get(name=site_name)
        tool_name = request.POST.get('tool_name')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        
        ToolAdd = Tool(site=site_name2, name=tool_name, quantity=quantity, amount=amount)
        ToolAdd.save()
        return redirect('ManageSites',site_id=site_id)

    return render(request,'sites/AddToolsPage.html',{'siteInfo':siteInfo})

def LabourDetails(request,labour_id):
    
    manPK = get_object_or_404(Manpower, pk=labour_id)

    if request.method == 'POST':
        manpower_id = request.POST.get('manpower_id')
        date_str = request.POST.get('date')
        # Convert the date to YYYY-MM-DD format
        date = datetime.strptime(date_str, '%b %d, %Y').strftime('%Y-%m-%d')
        present_or_absent = request.POST.get('present_or_absent')
        overtime = request.POST.get('overtime')
        amount_taken = request.POST.get('amount_taken')
        per_day_wages = request.POST.get('per_day_wages')

        try:
            manpower = Manpower.objects.get(pk=manpower_id)
        except Manpower.DoesNotExist:
            # Handle the case where the manpower_id is invalid
            return HttpResponse('Invalid manpower ID')

        # Create an instance of the Attendance model
        attendance = Attendance(
            manpower=manpower,
            date=date,
            present_or_absent=present_or_absent,
            overtime=overtime,
            amount_taken=amount_taken,
            per_day_wages=per_day_wages
        )
        attendance.save()

        return redirect('LabourDetails',labour_id =labour_id)

    manAttendances = Attendance.objects.filter(manpower=manPK)

    return render(request,'sites/LabourDetails.html',{'manPK':manPK,'manAttendances':manAttendances})

def delete_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    site.delete()
    return redirect('sites')

def delete_dataManage(request,delete_type, man_id, site_id):

    if delete_type == 'manpower':
        data = get_object_or_404(Manpower, pk=man_id)
    elif delete_type == 'expense':
        data = get_object_or_404(Expense, pk=man_id)
    elif delete_type == 'tool':
         data = get_object_or_404(Tool, pk=man_id)

    data.delete()
    return redirect('ManageSites',site_id=site_id)




