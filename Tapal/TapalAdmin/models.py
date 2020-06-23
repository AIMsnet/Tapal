from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date


class User(AbstractUser):
    username    =   None
    email       =   models.EmailField(max_length=255,null=False, unique=True)
    mobile_no   =   models.CharField(max_length=100, null=False, unique=True)
    employee_id =   models.CharField(max_length=50,null=False, unique=True)
    role        =   models.CharField(max_length=50, null=False)
    designation =   models.CharField(max_length=50, null=False)
    desk_id        =   models.CharField(max_length=50, null=False)
    user_id     =   models.CharField(max_length=100, null=False, unique=True)


    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS =  []
 

class InwardReg(models.Model):
    #Id     =  models.AutoField(null= False)
    RecRefNumber  =  models.CharField(("Recieved Reference Number"),default='AIM-0001', max_length=10, null=False)
    LttrRecDate   =   models.DateField(("Letter Recieved Date"), default=datetime.now)
    LatterDetails    = models.TextField(("Letter Details"), default='xyz', null=False)
    EmailId =   models.EmailField(("E-mail ID"), default='xyz@gmail.com',max_length=254)
    Address =   models.CharField(("Address"), default='Pune', max_length=200)
    TYPE_OF_REF= [
        ('Internal', 'Internal'),
        ('External', 'External'),
        ]
    TypeOfReference = models.CharField(("Type Of Reference"),max_length=10, choices=TYPE_OF_REF)
    RecDate   =    models.DateField(("Recieved Date"), default=datetime.now)
    RecFrom    =   models.CharField(("Recieved From"), default='user-1',max_length=100)
    MobileNumber    =   models.CharField(("Mobile Number"), default='8766518297',max_length=10)
    Dept= [
        ('Department1', 'Department1'),
        ('Department2', 'Department2'),
        ]
    RecFromDept =   models.CharField(("Received From Department"),max_length=20, choices=Dept)
    priority= [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
        ]
    Priority        =   models.CharField(("Priority"),max_length=20, choices=priority)
    Desk_id         =   models.CharField(("Desk_id"),max_length=20)
    users= [
        ('user-1', 'user-1'),
        ('user-2', 'user-2'),
        ('user-3', 'user-3'),
        ('user-4', 'user-4')
        ]
    users     =   models.CharField((''),max_length=20, choices=users)
    user_id         =   models.CharField(('user_id'),default='0000000',max_length=20)
    Status      =   models.CharField(max_length=20, default='Activated')
    
class InwardDocs(models.Model):
    InwardId    =   models.ForeignKey(to=InwardReg, on_delete=models.CASCADE)
    AttchedDate   =   models.DateField(("Document Attached Date"), default=datetime.now)
    DocsAttch   =   models.FileField(("Attached Documents"), upload_to='documents', max_length=100, null=True , blank=True)
    user_id         =   models.CharField(('user_id'),default='0000000',max_length=20)

class OutwardReg(models.Model):
    OutwardDate     =   models.DateField(("Outward Date"), default=datetime.now, null=False)
    Note            =   models.TextField(("Forwarding Note"), default='xyz', null=False)
    OutwardTo       =   models.CharField(("Outward To"), max_length=50)
    OutwardBy       =   models.CharField(("Outward By"), max_length=20)
    OutwardDoc      =   models.FileField(("Documents"), max_length=20)
    InwardId        =   models.IntegerField(("Inward ID"), null=True)
    History         =   models.TextField(("History"), default='xyz', null=False)
    Status          =   models.CharField(max_length=20, default='Activated')
