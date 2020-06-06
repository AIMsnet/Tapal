from django.urls import path
from django.conf.urls import url
from . import views
# from .views import CustomLogin
from django.contrib.auth import views as auth_views

urlpatterns = [

# MENU FORMS

    path('home/', views.home),
    path('inwardForm/', views.inwardForm),
    path('inwardForm/inwardForm/', views.inwardForm),
    path('inwardForm/inwardForm/inwardForm/', views.inwardForm),
    path('inwardForm/inwardForm/inwardForm/inwardForm/', views.inwardForm),

    path('manageDepartment/', views.manageDepartment),
    path('manageDepartment/manageDepartment/', views.manageDepartment),
    path('manageDepartment/manageDepartment/manageDepartment/', views.manageDepartment),
    path('manageDepartment/manageDepartment/manageDepartment/manageDepartment/', views.manageDepartment),
    path('manageDepartment/manageDepartment/manageDepartment/manageDepartment/manageDepartment/', views.manageDepartment),
    
    path('outwardRegistery/', views.outwardRegistery),
    path('ticketPurcahesInformation/', views.ticketPurcahesInformation),
    
    path('report/', views.report),
    path('report/report/', views.report),
    path('report/report/report/', views.report),

    path('changePassword/', views.changePassword),
    path('InwrdOtwrdDetails/', views.InwrdOtwrdDetails),
    path('receipt/', views.receipt),
    path('SendingDetails/', views.SendingDetails),
    path('EditTicketDetails/', views.EditTicketDetails),
    
    
    path('DeptHome/', views.DeptHome),
    path('deptInwardReg/', views.deptInwardReg),
    path('DeptReport/', views.DeptReport),
    path('actionToBeTaken/', views.actionToBeTaken),

    # path('BranchMaster', views.BranchMaster),
    # path('InwordDoc', views.InwordDoc),
    # path('MonitorLatter', views.MonitorLatter),
    # path('UserReg', views.UserReg),

    path('CreateUser/', views.createUser),
    path('CreateUser/CreateUser/', views.createUser),
    path('CreateUser/CreateUser/CreateUser/', views.createUser),
    path('CreateUser/CreateUser/CreateUser/CreateUser/', views.createUser),
    path('CreateUser/CreateUser/CreateUser/CreateUser/CreateUser/', views.createUser),

    # path('', CustomLogin.as_view(template_name='LoginForm.html'), name='login'),

    path('', auth_views.LoginView.as_view(template_name='LoginForm.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='LoginForm.html'), name='login'),
    # path('login/login/', auth_views.LoginView.as_view(template_name='LoginForm.html'), name='login'),
    # path('login/login/login/', auth_views.LoginView.as_view(template_name='LoginForm.html'), name='login'),
    # path('login/login/login/login/', auth_views.LoginView.as_view(template_name='LoginForm.html'), name='login'),
    # path('login/login/login/login/login/', auth_views.LoginView.as_view(template_name='LoginForm.html'), name='login'),

    
    path('logout/', views.logout),

    path('forward/', views.forward),
]