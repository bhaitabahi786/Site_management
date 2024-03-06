
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('addSites/', views.addSites, name='addSites'),
    path('ManageSites/<int:site_id>', views.ManageSites, name='ManageSites'),
    path('ManageSites/AddExpenses/', views.AddExpenses, name='AddExpenses'),
    path('ManageSites/AddManpower/<int:site_id>', views.AddManpower, name='AddManpower'),
    path('ManageSites/AddTools/', views.AddTools, name='AddTools'),
    path('ManageSites/LabourDetails/', views.LabourDetails, name='LabourDetails'),
    path('delete_site/<int:site_id>/', views.delete_site, name='delete_site'),
    path('delete_Manpower/<int:man_id>/<int:site_id>', views.delete_Manpower, name='delete_Manpower'),
        
]

