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
import json
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
from Tapal import settings


class CustomLogin(auth_views.LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())
        print('userlogin')
        if not self.request.user.is_superuser:
            self.request.session['username'] = self.request.user.username
            print(self.request.session['username'])
            # return HttpResponseRedirect(self.get_success_url())
            return HttpResponseRedirect(settings.cutomer_url)
        else:
            messages.error(self.request, 'Enter valid "USERNAME" and "PASSWARD"')
            # auth.logout(self.request)
            return redirect("/")

class AdminLogin(auth_views.LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())
        if self.request.user.is_superuser:
            self.request.session['email'] = self.request.user.email
            print(self.request.session['email'])
            # return HttpResponseRedirect(self.get_success_url())
            return HttpResponseRedirect(settings.admin_url)

        else:
            messages.error(self.request, 'Enter valid "USERNAME" and "PASSWARD"')
            # auth.logout(self.request)
            return redirect("/adminLogin/")

def createUser(request):
    if request.session.has_key('email'):
        form = createUserForms()
        if request.method == 'POST':
            print('insude if post')
            form = createUserForms(request.POST or None)
            print('form')
            if form.is_valid():
                print('form is valid')
                form = form.save()
                # username = form.cleaned_data['username']
                # messages.success(request, f'Your account has been created ! You are now able to login {username}!')
                print('saved')
                return redirect('/')
            else:
                print('invalid')
                print(form.errors)
        else:
            form = createUserForms()
        return render (request, "CreateUser.html", {'form' : form})
    return redirect("/adminLogin/")

def logout(request):   
    print('logging out')
    request.session.flush()
    print("Session flushed")
    auth.logout(request)
    return redirect('/')

def logoutAdmin(request):
    print('logging out admin')
    request.session.flush()
    print("Session flushed")
    auth.logout(request)
    return redirect('/DeptHome/')

def home(request):
    if request.session.has_key('username'):
        return render(request, "home.html")
    return redirect("/")

def inwardForm(request):
    if request.session.has_key('username'):
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
                    username     =   request.user.username
                    print(desk_id, username)
            
                obj =   form.save()
                docs = DocForm.cleaned_data['DocsAttch']
                InwardDocs.objects.create(InwardId = obj, DocsAttch = docs, user_id = username)
                obj.username = username
                obj.save()
                a = messages.success(request, "Latter Inwarded")
                return redirect('inwardForm/', {'a': a})
            else:
                messages.error(request, "Please Re-enter Something Went Wrong")
                print(form.errors.as_json)
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
            username     =   request.user.username
            print(desk_id, username)
            
        if form.is_valid():
            obj =   form.save()
            obj.username = username
            obj.save()
    else:
        form = forwardForm()
        return render(request, "manageDepartment.html" )

def manageDepartment(request):
    if request.session.has_key('username'):
        # FETCHING USERS FROM DB
        users   =   User.objects.all()
        # Dropdown select user to forward
        userToFrwrd   =   User.objects.exclude(username=request.user.username)

        outwardForm = OutwardForm()
        
        # GETTING CREDENTIALS OF LOGGED IN USER
        if request.user.is_authenticated :
                desk_id     =   request.user.desk_id
                username     =   request.user.username
        
        records  =   InwardReg.objects.filter(user_id = username)

        # FORWARD RECORD
        if request.method == 'POST' and 'buttonForward' in request.POST:
            print('inside Forward')
            SelectedUser    = request.POST.get('selectUser')
            buttonForward   =  request.POST.get('buttonForward')

            print(SelectedUser)
            print(buttonForward)

            updateRecord   =    InwardReg.objects.get(id = buttonForward)
            updateRecord.user_id    =   SelectedUser
            updateRecord.RecievedFrom   =   username
            updateRecord.save()

            records  =   InwardReg.objects.filter(user_id=username)

            context ={
                'records'   : records,
                'userToFrwrd'     : userToFrwrd,
                'outwardForm'   : outwardForm
            }
            return render(request, "manageDepartment.html",context)

        # EIDT INWARD RECORD 
        if request.method == 'POST' and 'saveModelButton' in request.POST:
            print("inside modelsave")

            SelectedUser   =    request.POST.get('saveModelButton')
            updateText     =    request.POST.get('updateText')
            DocsAttch      =    request.FILES.get('DocsAttch')
            status         =    request.POST.get('status')
            
            addUpdate      =    InwardReg.objects.get(id = SelectedUser)
            dat = addUpdate.LatterDetails
            tm = time.strftime('%d %b %Y')
            addUpdate.LatterDetails   =   dat + "\n"+ username + " : " + tm + " : " + updateText
            addUpdate.save()

            inwardReg = InwardReg.objects.get(id = SelectedUser) 
            inwardDocs =  InwardDocs.objects.create(InwardId = inwardReg, DocsAttch = DocsAttch, user_id = username)
            
            context ={
                'records'       : records,
                'users'         : users,
                'outwardForm'   : outwardForm
            }
            return render(request, "manageDepartment.html",context)

        # RECORD OUTWARDING 
        if request.method == 'POST' and 'outwardBtn' in request.POST:
            print("inside Outward")
            outwardForm = OutwardForm(request.POST, request.FILES or None) 
            inwardId    = request.POST.get('txtinwrdid')
            history     = request.POST.get('txtOutwrdHistory')
            status         =    request.POST.get('statusOutwrd')
            print(status)
            
            if outwardForm.is_valid():
                obj =   outwardForm.save()
                obj.OutwardBy = username
                obj.InwardId  = inwardId
                obj.History =   history
            # ----------------------Activate/Deactivate----------------------
                if status is not None:
                    obj.Status   = "False"
                else:
                    obj.Status   = "True"
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

        # ACTIVATE / DEACTIVATE
        if request.method == 'POST' and 'buttonId' in request.POST:
            print('inside userlist')
            
            changeFor   =   request.POST.get('buttonId')
            print(changeFor)

            toChange    =   request.POST.get('changeTo')
            print(toChange)

            inwardReg = InwardReg.objects.get(id = changeFor)
            inwardReg.Status = toChange
            inwardReg.save()

            context ={
                'records'       : records,
                'users'         : users,
                'outwardForm'  : outwardForm  
            }
            return render(request, "manageDepartment.html", context)

        # SEARCH RECORD
        if request.method == 'POST' and 'btnSearch' in request.POST:
            searchString =  request.POST.get('searchString')
            print(searchString)
            
            #check searching string is an integer or string

            if searchString.isnumeric():
                print("is integer")
                records  =   InwardReg.objects.filter(user_id = username).filter(Q(id = searchString)| Q(MobileNumber = searchString))
            else:
                print("is string")
                records  =   InwardReg.objects.filter(user_id = username).filter(Q(Status = searchString)| Q(Priority = searchString))
            
            context ={
                'records'   : records,
                'users'     : users,
                'outwardForm'   : outwardForm
            }
            return render(request, "manageDepartment.html",context)


        else:
            context ={
                'records'   : records,
                'users'     : users,
                'userToFrwrd' : userToFrwrd,
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
  
    if request.session.has_key('username'):
        if request.user.is_authenticated :
                username     =   request.user.username
        outwardData = OutwardReg.objects.filter(OutwardBy = username)

        if request.method == 'POST':
            print("outward")
            inwardId    = request.POST.get('value')
            status      = request.POST.get('status')
            print(status)

            outwardData = OutwardReg.objects.filter(OutwardBy = username)
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

def report(request):
    if request.session.has_key('username'):

        if request.user.is_authenticated :
                desk_id     =   request.user.desk_id
                username     =   request.user.username
                print(desk_id, username)

        if request.method == 'POST' :
            
            startDate   = request.POST.get('strtdt')
            endDate   = request.POST.get('enddt')

            records  =   InwardReg.objects.filter(LttrRecDate__range=(startDate, endDate), user_id=username)
            
            context ={
                'records'   : records,          
            }
            return render(request, "report.html",context)
        else:
            
            return render(request, "report.html")
    return redirect('/')

def DeptHome(request):
    if request.session.has_key('email'):
        return render(request, 'DeptHome.html')
    return redirect("/adminLogin/")

def DeptReport(request):
    if request.session.has_key('email'):
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
    return redirect("/adminLogin/")

def adminManageRegistry(request):

    if request.session.has_key('email'):
        # FETCHING USERS FROM DB
        users   =   User.objects.all()

        outwardForm = OutwardForm()
        outwardForm = OutwardForm(request.POST, request.FILES or None) 

        # GETTING CREDENTIALS OF LOGGED IN USER
        if request.user.is_authenticated :
                desk_id     =   request.user.desk_id
                username     =   request.user.username
        
        records  =   InwardReg.objects.all

        # FORWARD RECORD
        if request.method == 'POST' and 'buttonForward' in request.POST:
            print('inside Forward')
            SelectedUser    = request.POST.get('selectUser')
            buttonForward   =  request.POST.get('buttonForward')

            print(SelectedUser)
            print(buttonForward)

            updateRecord   =    InwardReg.objects.get(id = buttonForward)
            updateRecord.user_id    =   SelectedUser
            updateRecord.RecievedFrom   =   username
            updateRecord.save()

            records  =   InwardReg.objects.all

            context ={
                'records'   : records,
                'users'     : users,
                'outwardForm'   : outwardForm
            }
            return render(request, "adminManageRegistry.html",context)

        # EIDT INWARD RECORD 
        if request.method == 'POST' and 'saveModelButton' in request.POST:
            print("inside modelsave")

            SelectedUser   =    request.POST.get('saveModelButton')
            updateText     =    request.POST.get('updateText')
            DocsAttch      =    request.FILES.get('DocsAttch')
            status         =    request.POST.get('status')
            
            addUpdate      =    InwardReg.objects.get(id = SelectedUser)
            dat = addUpdate.LatterDetails
            tm = time.strftime('%d %b %Y')
            addUpdate.LatterDetails   =   dat + "\n"+ username + " : " + tm + " : " + updateText
            addUpdate.save()

            inwardReg = InwardReg.objects.get(id = SelectedUser) 
            inwardDocs =  InwardDocs.objects.create(InwardId = inwardReg, DocsAttch = DocsAttch, user_id = username)
            
            context ={
                'records'       : records,
                'users'         : users,
                'outwardForm'   : outwardForm
            }
            return render(request, "adminManageRegistry.html",context)

        # RECORD OUTWARDING 
        if request.method == 'POST' and 'outwardBtn' in request.POST:
            print("inside Outward")
            outwardForm = OutwardForm(request.POST, request.FILES or None) 
            inwardId    = request.POST.get('txtinwrdid')
            history     = request.POST.get('txtOutwrdHistory')
            status         =    request.POST.get('statusOutwrd')
            print(status)
            
            if outwardForm.is_valid():
                obj =   outwardForm.save()
                obj.OutwardBy = username
                obj.InwardId  = inwardId
                obj.History =   history
            # ----------------------Activate/Deactivate----------------------
                if status is not None:
                    obj.Status   = "Deactivated"
                else:
                    obj.Status   = "Activate"
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
            return render(request, "adminManageRegistry.html", context)

        # ACTIVATE / DEACTIVATE
        if request.method == 'POST' and 'buttonId' in request.POST:
            print('inside userlist')
            
            changeFor   =   request.POST.get('buttonId')
            print(changeFor)

            toChange    =   request.POST.get('changeTo')
            print(toChange)

            inwardReg = InwardReg.objects.get(id = changeFor)
            inwardReg.Status = toChange
            inwardReg.save()

            context ={
                'records'       : records,
                'users'         : users,
                'outwardForm'  : outwardForm  
            }
            return render(request, "adminManageRegistry.html", context)

        # SEARCH RECORD
        if request.method == 'POST' and 'btnSearch' in request.POST:
            searchString =  request.POST.get('searchString')
            print(searchString)

            if searchString.isnumeric():
                print("is integer")
                records  =   InwardReg.objects.filter(user_id = username).filter(Q(id = searchString)| Q(MobileNumber = searchString))
            else:
                print("is string")
                records  =   InwardReg.objects.filter(user_id = username).filter(Q(Status = searchString)| Q(Priority = searchString))
            

            context ={
                'records'   : records,
                'users'     : users,
                'outwardForm'   : outwardForm
            }
            return render(request, "adminManageRegistry.html",context)


        else:
            context ={
                'records'   : records,
                'users'     : users,
                'outwardForm' : outwardForm,
            }
            return render(request, "adminManageRegistry.html", context)
    return redirect("/adminLogin/")

def adminOutwardRegistry(request):

    if request.session.has_key('email'):

        if request.user.is_authenticated :
                username     =   request.user.username
        outwardData = OutwardReg.objects.all

        if request.method == 'POST':
            print("outward")
            inwardId    = request.POST.get('value')
            status      = request.POST.get('status')
            print(status)

            outwardData = OutwardReg.objects.all
            records     = InwardReg.objects.get(id = inwardId)
            context =   {
                'outwardData' : outwardData,
                
            }
            return render(request, "adminOutwardRegistry.html", context)
        else:
            context =   {
                'outwardData' : outwardData,
            }
            return render(request, "adminOutwardRegistry.html", context)

    return redirect("/adminLogin/")
    
def DownloadFile(request, fileName):
    print("I m from view and file name is", fileName)
    file = "media/documents/" + fileName
    f = open(file)
    response = HttpResponse(f.read(), content_type='application/txt')
    response['Content-Length'] = os.path.getsize(file)
    response['Content-Disposition'] = 'attachment; filename=%s' % fileName
    return response

def DownloadOutwrdFile(request, fileName):
    print("I m from view and file name is", fileName)
    file = "media/" + fileName
    f = open(file)
    response = HttpResponse(f.read(), content_type='application/txt')
    response['Content-Length'] = os.path.getsize(file)
    response['Content-Disposition'] = 'attachment; filename=%s' % fileName
    return response

def UserList(request):
    if request.session.has_key('email'):
        users = User.objects.all

        if request.method == 'POST':
            print('inside userlist')
            toChange    =   request.POST.get('changeTo')
            print(toChange)

            changeFor   =   request.POST.get('buttonId')
            print(changeFor)
            
            changeStatus    =   User.objects.get(id = changeFor)
            changeStatus.is_active  = toChange
            changeStatus.save()

            context = {
                'users' : users
            }
            return render(request, "UserTable.html", context)
        else:
            context = {
                'users' : users
            }
            return render(request, "UserTable.html", context)
    return redirect("/adminLogin/")