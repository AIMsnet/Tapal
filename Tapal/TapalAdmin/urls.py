from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

# MENU FORMS

    path('', views.login),
    path('home', views.home),
    path('inwardForm', views.inwardForm),
    path('manageDepartment', views.manageDepartment),
    path('outwardRegistery', views.outwardRegistery),
    path('ticketPurcahesInformation', views.ticketPurcahesInformation),
    path('report', views.report),
    path('changePassword', views.changePassword),
    path('InwrdOtwrdDetails', views.InwrdOtwrdDetails),
    path('receipt', views.receipt),
    path('SendingDetails', views.SendingDetails),
    path('EditTicketDetails', views.EditTicketDetails),
    
    
    path('DeptHome', views.DeptHome),
    path('deptInwardReg', views.deptInwardReg),
    path('DeptReport', views.DeptReport),
    path('actionToBeTaken', views.actionToBeTaken),

    path('BranchMaster', views.BranchMaster),
    path('InwordDoc', views.InwordDoc),
    path('MonitorLatter', views.MonitorLatter),
    path('UserReg', views.UserReg)

]