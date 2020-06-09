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
from django.db.models import Q


class CustomLogin(auth_views.LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())
        self.request.session['user_id'] = self.request.user.user_id
        print(self.request.session['user_id'])
        return HttpResponseRedirect(self.get_success_url())

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
    print('logging out')
    request.session.flush()
    print("Session flushed")
    auth.logout(request)
    return redirect('/')

def home(request):
    if request.session.has_key('user_id'):
        return render(request, "home.html")
    return redirect("/")

def inwardForm(request):
    if request.session.has_key('user_id'):
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
    return redirect("/")


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
    if request.session.has_key('user_id'):

        users   =   User.objects.all()

        if request.user.is_authenticated :
                desk_id     =   request.user.desk_id
                user_id     =   request.user.user_id
                print(desk_id, user_id)

        records  =   InwardRegistry.objects.filter(user_id=user_id)

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
    return redirect("/")

def outwardRegistery(request):
    if request.session.has_key('user_id'):
        return render(request, "outwardRegistery.html")
    return redirect("/")

def ticketPurcahesInformation(request):
    if request.session.has_key('user_id'):
        return render(request, "ticketPurcahesInformation.html")
    return redirect("/")

def InwrdOtwrdDetails(request):
    if request.session.has_key('user_id'):
        return render(request, "InwrdOtwrdDetails.html")
    return redirect('/')

@login_required
def report(request):
    if request.session.has_key('user_id'):

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
            
            return render(request, "report.html")
    return redirect('/')
    
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

    if request.method == 'POST' :
        
        startDate   = request.POST.get('strtdt')
        endDate   = request.POST.get('enddt')

        records  =   InwardRegistry.objects.filter(ReferenceRecievedDate__range=(startDate, endDate))
        
        context ={
            'records'   : records,          
        }
        return render(request, "DeptReport.html",context)
    else:
        return render(request,'DeptReport.html')

def actionToBeTaken(request):
    return render(request, "ActionToBeTaken.html")

def adminManageRegistry(request):

    users   =   User.objects.all()
    records  =   InwardRegistry.objects.all

    if request.method == 'POST' and 'buttonForward' in request.POST:
        print('inside post')
        SelectedUser    = request.POST.get('selectUser')
        buttonForward   =  request.POST.get('buttonForward')

        updateRecord   =    InwardRegistry.objects.get(id = buttonForward)
        updateRecord.user_id    =   SelectedUser
        updateRecord.save()

        context ={
            'records'   : records,
            'users'     : users,
        }
        return render(request, "adminManageRegistry.html", context)

    elif request.method == 'POST' and 'buttonSearch' in request.POST:
        search    = request.POST.get('searchInput')

        if search.isnumeric():
            records = InwardRegistry.objects.filter(id = search) or InwardRegistry.objects.filter(MobileNumber = search)
        else:
         records = InwardRegistry.objects.filter(user_id = search) or InwardRegistry.objects.filter(EmailId = search)

        context ={
            'records'   : records,
            'users'      : users
        }
        return render(request, "adminManageRegistry.html", context)
    else:
        context ={
            'records'   : records,
            'users'     : users,
        }
        return render(request, "adminManageRegistry.html", context)

    