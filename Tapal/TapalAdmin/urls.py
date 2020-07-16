from django.urls import path
from django.conf.urls import url
from . import views
# from .views import CustomLogin
from django.contrib.auth import views as auth_views

urlpatterns = [

# USER
    path('', views.CustomLogin.as_view(template_name='LoginForm.html'), name='login'),
    path('home/', views.home),
    path('inwardForm/', views.inwardForm),
    path('inwardForm/inwardForm/', views.inwardForm),
    path('inwardForm/inwardForm/inwardForm/', views.inwardForm),
    path('manageDepartment/', views.manageDepartment),
    path('outwardRegistery/', views.outwardRegistery),
    path('report/', views.report),
    path('forward/', views.forward),
    path("getFile/", views.getFiles),
    url('file/(?P<fileName>[\w\s,@.]+)', views.DownloadFile, name = "showSupplier"),
    url('outwardFile/(?P<fileName>[\w\s,@.]+)', views.DownloadOutwrdFile, name = "showSupplier"),
    path('logout/', views.logout),    


# ADMINISTRATION
    path('adminLogin/', views.AdminLogin.as_view(template_name='adminLogin.html'), name='login'),
    path('DeptHome/', views.DeptHome),
    path('CreateUser/', views.createUser),
    path('adminManageRegistry/', views.adminManageRegistry),
    path('adminOutwardRegistry/', views.adminOutwardRegistry),
    path('DeptReport/', views.DeptReport),
    path('userList/', views.UserList),
    path('logoutAdmin/', views.logoutAdmin),

    
]