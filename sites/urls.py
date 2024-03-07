
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('sites', views.sites, name='sites'),
    path('addSites/', views.addSites, name='addSites'),
    path('ManageSites/<int:site_id>', views.ManageSites, name='ManageSites'),
    path('ManageSites/AddExpenses/<int:site_id>', views.AddExpenses, name='AddExpenses'),
    path('ManageSites/AddManpower/<int:site_id>', views.AddManpower, name='AddManpower'),
    path('ManageSites/AddTools/<int:site_id>', views.AddTools, name='AddTools'),
    path('delete_site/<int:site_id>/', views.delete_site, name='delete_site'),
    path('delete_dataManage/<str:delete_type>/<int:man_id>/<int:site_id>', views.delete_dataManage, name='delete_dataManage'),
    path('ManageSites/LabourDetails/<int:labour_id>', views.LabourDetails, name='LabourDetails'),
    
]

