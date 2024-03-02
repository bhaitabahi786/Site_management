
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    # path('addSites/', views.addSites, name='addSites'),
    # path('ManageSites/', views.ManageSites, name='ManageSites'),
    # path('AddExpenses/', views.AddExpenses, name='AddExpenses'),
    # path('AddManpower/', views.AddManpower, name='AddManpower'),
    # path('AddTools/', views.AddTools, name='AddTools'),
    
]

