
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
    path('ManageSites/<int:site_id>/LabourDetails/<int:labour_id>', views.LabourDetails, name='LabourDetails'),

    # delete view urls
    path('delete_site/<int:site_id>', views.delete_site, name='delete_site'),
    path('delete_dataManage/<str:delete_type>/<int:man_id>/<int:site_id>', views.delete_dataManage, name='delete_dataManage'),
    path('delete_ManData/<int:site_id>/<int:labour_id>/<int:record_id>', views.delete_ManData, name='delete_ManData'),

    # edit view urls
    path('editSites/<int:site_id>', views.editSites, name='editSites'),
    path('ManageSites/EditExpenses/<int:expense_id>/<int:site_id>', views.EditExpenses, name='EditExpenses'),
    path('ManageSites/EditTools/<int:tool_id>/<int:site_id>', views.EditTools, name='EditTools'),
    path('ManageSites/EditManpower/<int:manpower_id>/<int:site_id>', views.EditManpower, name='EditManpower'),
    path('ManageSites/<int:site_id>/EditLabourDetails/<int:labour_id>/<int:record_id>', views.EditLabourDetails, name='EditLabourDetails'),
   
]

