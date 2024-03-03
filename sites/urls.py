
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('addSites/', views.addSites, name='addSites'),
    path('ManageSites/', views.ManageSites, name='ManageSites'),
    path('ManageSites/AddExpenses/', views.AddExpenses, name='AddExpenses'),
    path('ManageSites/AddManpower/', views.AddManpower, name='AddManpower'),
    path('ManageSites/AddTools/', views.AddTools, name='AddTools'),
    path('ManageSites/LabourDetails/', views.LabourDetails, name='LabourDetails'),
        
]
