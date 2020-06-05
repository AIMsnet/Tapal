from django.shortcuts import render,redirect
from .forms import InwardRegistryForm,BranchMasterForm, InwordDocForm, MonitorLatterForm, UserRegForms
from django.contrib import messages

# InwardRegistryForm,

from django.db import connections

# Create your views here.

def login(request):
    return render(request, "LoginForm.html")

def home(request):
    return render(request, "home.html")

def inwardForm(request):
    form=InwardRegistryForm()
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM branch_master")
    a = cursor.fetchall()
    print(a)
    if request.method == 'POST':
        form = InwardRegistryForm(request.POST or None)
        if form.is_valid():
            print('form is valid')
            
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Your account has been created ! You are now able to login {username}!')
            print('saved')
            return redirect('inwardForm/')
        
    else:
        form = InwardRegistryForm()
    return render(request, "InwardForm.html",{'form' : form, 'a' : a})

def manageDepartment(request):
    return render(request, "manageDepartment.html")

def outwardRegistery(request):
    return render(request, "outwardRegistery.html")

def ticketPurcahesInformation(request):
    return render(request, "ticketPurcahesInformation.html")

def InwrdOtwrdDetails(request):
    return render(request, "InwrdOtwrdDetails.html")

def report(request):
    return render(request, "report.html")
    
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


def BranchMaster(request):
    form = BranchMasterForm()
    return render(request, "branchMasterForm.html", {'form' : form})

def InwordDoc(request):
    form = InwordDocForm()
    return render(request, "InwordDocForm.html", {'form' : form})

def MonitorLatter(request):
    form = MonitorLatterForm()
    return render(request, "MonitorLatterForm.html", {'form' : form})

def UserReg(request):
    form = UserRegForms()
    return render (request, "UserRegForms.html", {'form' : form})
    
