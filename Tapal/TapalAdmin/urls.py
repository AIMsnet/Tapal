from django.urls import path
from django.conf.urls import url
from . import views
# from .views import CustomLogin
from django.contrib.auth import views as auth_views

urlpatterns = [

# MENU FORMS

    path('', auth_views.LoginView.as_view(template_name='LoginForm.html'), name='login'),

    path('home/', views.home),
    path('inwardForm/', views.inwardForm),
    path('manageDepartment/', views.manageDepartment),
    path('outwardRegistery/', views.outwardRegistery),
    path('ticketPurcahesInformation/', views.ticketPurcahesInformation),
    
    path('report/', views.report),
    # path('report/report/', views.report),
    # path('report/report/report/', views.report),

    path('changePassword/', views.changePassword),
    path('InwrdOtwrdDetails/', views.InwrdOtwrdDetails),
    path('receipt/', views.receipt),
    path('SendingDetails/', views.SendingDetails),
    path('EditTicketDetails/', views.EditTicketDetails),

    path('CreateUser/', views.createUser),

    
    path('logout/', views.logout),
    path('forward/', views.forward),

    # ADMINISTRATION
    path('adminManageRegistry/', views.adminManageRegistry),
    
    path('DeptHome/', views.DeptHome),
    path('deptInwardReg/', views.deptInwardReg),
    path('DeptReport/', views.DeptReport),
    path('actionToBeTaken/', views.actionToBeTaken),

]