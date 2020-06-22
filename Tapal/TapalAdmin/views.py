from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect
from .forms import createUserForms, InwardRegistryForm,forwardForm, InwardDocForm, OutwardForm
from .models import InwardReg, User, InwardDocs, OutwardReg
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import  LoginView
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
import time as time
from django.utils.dateparse import parse_date
from django.db.models import Q
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
import json # for json dumps
from django.core import serializers

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
        print("Inside inward ")
        form = InwardRegistryForm()
        DocForm = InwardDocForm()

        if request.method == 'POST':
            print('a')
            form = InwardRegistryForm(request.POST, request.FILES or None)
            DocForm = InwardDocForm(request.POST, request.FILES or None)
            print('b')
            if form.is_valid() and DocForm.is_valid():
                print('form is valid')
                if request.user.is_authenticated :
                    desk_id     =   request.user.desk_id
                    user_id     =   request.user.user_id
                    print(desk_id, user_id)
            
                obj =   form.save()
                docs = DocForm.cleaned_data['DocsAttch']
                InwardDocs.objects.create(InwardId = obj, DocsAttch = docs, user_id = user_id)
                obj.user_id = user_id
                obj.save()
                messages.success(request, "Latter Inwarded")
                return redirect('inwardForm/')
            else:
                messages.error(request, "Please Re-enter Something Went Wrong")
                print(form.errors)
                print('c')
        else:
            print('d')
            form = InwardRegistryForm()
            DocForm  = InwardDocForm()
        return render(request, "InwardForm.html",{'form' : form, 'DocForm' : DocForm})
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

        outwardForm = OutwardForm()
        outwardForm = OutwardForm(request.POST, request.FILES or None) 

        if request.user.is_authenticated :
                desk_id     =   request.user.desk_id
                user_id     =   request.user.user_id
        
        records  =   InwardReg.objects.filter(user_id=user_id)
 
        if request.method == 'POST' and 'buttonForward' in request.POST:
            print('inside Forward')
            SelectedUser    = request.POST.get('selectUser')
            buttonForward   =  request.POST.get('buttonForward')

            print(SelectedUser)
            print(buttonForward)

            updateRecord   =    InwardReg.objects.get(id = buttonForward)
            updateRecord.user_id    =   SelectedUser
            updateRecord.RecievedFrom   =   user_id
            updateRecord.status         =   "Unseen"
            updateRecord.save()

            records  =   InwardReg.objects.filter(user_id=user_id)

            context ={
                'records'   : records,
                'users'     : users,
                'outwardForm'   : outwardForm
            }
            return render(request, "manageDepartment.html",context)

        if request.method == 'POST' and 'saveModelButton' in request.POST:
            print("inside modelsave")

            SelectedUser   =    request.POST.get('saveModelButton')
            updateText     =    request.POST.get('updateText')
            DocsAttch        =    request.FILES.get('DocsAttch')
            
            addUpdate      =    InwardReg.objects.get(id = SelectedUser)
            dat = addUpdate.LatterDetails
            tm = time.strftime('%d %b %Y')
            addUpdate.LatterDetails   =   dat + "\n"+ user_id + " : " + tm + " : " + updateText
            addUpdate.save()

            inwardReg = InwardReg.objects.get(id = SelectedUser)
            
            inwardDocs =  InwardDocs.objects.create(InwardId = inwardReg, DocsAttch = DocsAttch, user_id = user_id)
            
            context ={
                'records'       : records,
                'users'         : users,
                'outwardForm'   : outwardForm
            }
            return render(request, "manageDepartment.html",context)

        if request.method == 'POST' and 'outwardBtn' in request.POST:
            print("inside Outward")
            outwardForm = OutwardForm(request.POST, request.FILES or None) 
            inwardId    = request.POST.get('txtinwrdid')
            history     = request.POST.get('txtOutwrdHistory')

            if outwardForm.is_valid():
                obj =   outwardForm.save()
                obj.OutwardBy = user_id
                obj.InwardId  = inwardId
                obj.History =   history
                obj.save()
                outwardTo = outwardForm.cleaned_data['OutwardTo']
                updateRecord   =    InwardReg.objects.get(id = inwardId)
                updateRecord.user_id    =   outwardTo
                updateRecord.save()

            context ={
                'records'       : records,
                'users'         : users,
                'outwardForm'  : outwardForm  
            }
            return render(request, "manageDepartment.html", context)

        else:
            context ={
                'records'   : records,
                'users'     : users,
                'outwardForm' : outwardForm,
            }
            return render(request, "manageDepartment.html", context)
    return redirect("/")


def getFiles(request):
    if request.method == 'POST':
        inwardDocs = InwardDocs.objects.filter(InwardId = request.POST['inwardId'])
        inwardDocs = serializers.serialize('json', inwardDocs)
        inwardDocs = json.loads(inwardDocs)
        response = {'status' : 0, 'inwardDocs' : inwardDocs}
    return HttpResponse(json.dumps(response), content_type = 'application/json')

def outwardRegistery(request):
  
    if request.session.has_key('user_id'):
        if request.user.is_authenticated :
                user_id     =   request.user.user_id
        outwardData = OutwardReg.objects.filter(OutwardBy = user_id)

        if request.method == 'POST':
            inwardId    = request.POST.get('value')

            outwardData = OutwardReg.objects.filter(OutwardBy = user_id)
            records     = InwardReg.objects.get(id = inwardId)
            context =   {
                'outwardData' : outwardData,
                
            }
            return render(request, "outwardRegistery.html", context)
        else:
            context =   {
                'outwardData' : outwardData,
            }
            return render(request, "outwardRegistery.html", context)
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

            records  =   InwardReg.objects.filter(LttrRecDate__range=(startDate, endDate), user_id=user_id)
            
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

        records  =   InwardReg.objects.filter(LttrRecDate__range=(startDate, endDate))
        
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
    records  =   InwardReg.objects.all

    if request.method == 'POST' and 'buttonForward' in request.POST:
        print('inside post')
        SelectedUser    = request.POST.get('selectUser')
        buttonForward   =  request.POST.get('buttonForward')

        updateRecord   =    InwardReg.objects.get(id = buttonForward)
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
            records = InwardReg.objects.filter(id = search) or InwardReg.objects.filter(MobileNumber = search)
        else:
         records = InwardReg.objects.filter(user_id = search) or InwardReg.objects.filter(EmailId = search)

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

def DownloadFile(request, fileName):
    print("I m from view and file name is", fileName)
    file = "media/documents/" + fileName
    f = open(file)
    response = HttpResponse(f.read(), content_type='application/txt')
    response['Content-Length'] = os.path.getsize(file)
    response['Content-Disposition'] = 'attachment; filename=%s' % fileName
    return response