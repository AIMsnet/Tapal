from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect
# from .forms import InwardRegistryForm,BranchMasterForm, InwordDocForm, MonitorLatterForm, UserRegForms, createUserForms
from .forms import createUserForms, InwardRegistryForm,forwardForm
from .models import InwardRegistry, User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from datetime import date,datetime
import datetime
from django.utils.dateparse import parse_date

# from django.db import connections

# # Create your views here.

# def login1(request):
#     return render(request, "LoginForm.html")

def home(request):
    return render(request, "home.html")

def inwardForm(request):
    form=InwardRegistryForm()
    if request.method == 'POST':
        print('a')
        form = InwardRegistryForm(request.POST or None)
        print('b')
        if form.is_valid():
            print('form is valid')
            if request.user.is_authenticated :
                desk_id     =   request.user.desk_id
                user_id     =   request.user.user_id
                print(desk_id, user_id)
           
            obj =   form.save()
            obj.user_id = user_id
            obj.save()
           
            print('saved')
            return redirect('inwardForm/')
        else:
            print(form.errors)
            print('c')
    else:
        print('d')
        form = InwardRegistryForm()
    return render(request, "InwardForm.html",{'form' : form})

def forward(request):
    
    if request.method == 'POST':
        # selectedUser    = 
        form = forwardForm(request.POST or None)
        if request.user.is_authenticated :
            desk_id     =   request.user.desk_id
            user_id     =   request.user.user_id
            print(desk_id, user_id)
            
        if form.is_valid():
            obj =   form.save()
            obj.user_id = user_id
            obj.save()
    else:
        form = forwardForm()
        return render(request, "manageDepartment.html" )

@login_required
def manageDepartment(request):

    users   =   User.objects.all()

    if request.user.is_authenticated :
            desk_id     =   request.user.desk_id
            user_id     =   request.user.user_id
            print(desk_id, user_id)

    records  =   InwardRegistry.objects.filter(user_id=user_id)
    print("a")

    if request.method == 'POST':
        print('inside post')
        SelectedUser    = request.POST.get('selectUser')
        buttonForward   =  request.POST.get('buttonForward')
    

        updateRecord   =    InwardRegistry.objects.get(id = buttonForward)
        updateRecord.user_id    =   SelectedUser
        updateRecord.save()

        records  =   InwardRegistry.objects.filter(user_id=user_id)

        context ={
            'records'   : records,
            'users'     : users,
        }

        return render(request, "manageDepartment.html", context)
   
    else:
        context ={
            'records'   : records,
            'users'     : users,
        }
        return render(request, "manageDepartment.html", context)

def outwardRegistery(request):
    return render(request, "outwardRegistery.html")

def ticketPurcahesInformation(request):
    return render(request, "ticketPurcahesInformation.html")

def InwrdOtwrdDetails(request):
    return render(request, "InwrdOtwrdDetails.html")

@login_required
def report(request):
    if request.user.is_authenticated :
            desk_id     =   request.user.desk_id
            user_id     =   request.user.user_id
            print(desk_id, user_id)

    if request.method == 'POST' :
        
        startDate   = request.POST.get('strtdt')
        endDate   = request.POST.get('enddt')

        records  =   InwardRegistry.objects.filter(ReferenceRecievedDate__range=(startDate, endDate), user_id=user_id)
        
        context ={
            'records'   : records,          
        }
        return render(request, "report.html",context)
    else:
        context ={
            'records'   : records,          
        }
        return render(request, "report.html", context)
    
def changePassword(request):
    return render(request, "changePassword.html")

def receipt(request):
    return render(request, "receipt.html")

def SendingDetails(request):
    return render(request, "SendingDetails.html")

def EditTicketDetails(request):
    return render(request, 'EditTicketDetails.html')


def DeptHome(request):
    return render(request, 'DeptHome.html')

def deptInwardReg(request):
    return render(request, 'deptInwardReg.html')

def DeptReport(request):
    return render(request,'DeptReport.html')

def actionToBeTaken(request):
    return render(request, "ActionToBeTaken.html")


# def BranchMaster(request):
#     form = BranchMasterForm()
#     return render(request, "branchMasterForm.html", {'form' : form})

# def InwordDoc(request):
#     form = InwordDocForm()
#     return render(request, "InwordDocForm.html", {'form' : form})

# def MonitorLatter(request):
#     form = MonitorLatterForm()
#     return render(request, "MonitorLatterForm.html", {'form' : form})

# def UserReg(request):
#     form = UserRegForms()
#     return render (request, "UserRegForms.html", {'form' : form})

def createUser(request):
    form = createUserForms()
    if request.method == 'POST':
        print('insude if post')
        form = createUserForms(request.POST or None)
        print('form')
        if form.is_valid():
            print('form is valid')
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Your account has been created ! You are now able to login {username}!')
            print('saved')
            return redirect('/')
        else:
            print('invalid')
            print(form.errors)
    else:
        form = createUserForms()
    return render (request, "CreateUser.html", {'form' : form})
    
def logout(request):
    auth.logout(request)
    return redirect('/')


# class CustomLogin(auth_views.LoginView):
#     print('a')
#     def form_valid(self, form):
#          login(self.request, form.get_user())
#         #  print()
#         #  self.request.session['userid']    =  user.first_name
#         #  print()
#          return HttpResponseRedirect(self.get_success_url())
