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
    #InwardNumber     =  models.AutoField(null= False)
    RecRefNumber  =  models.IntegerField(("Recieved Reference Number"),default='0000001', null=False)
    LttrRecDate   =   models.DateField(("Latter Recieved Date"), default=datetime.now)
    LatterDetails    = models.TextField(("Latter Details"), default='xyz', null=False)
    EmailId =   models.EmailField(("E-mail ID"), default='xyz@gmail.com',max_length=254)
    Address =   models.CharField(("Address"), default='Pune', max_length=200)
    TYPE_OF_REF= [
        ('Internal', 'Internal'),
        ('Govt', 'Govt'),
        ]
    TypeOfReference = models.CharField(("Type Of Reference"),max_length=10, choices=TYPE_OF_REF)
    RecDate   =    models.DateField(("Reference Date"), default=datetime.now)
    RecFrom    =   models.CharField(("Recieved From"), default='user-1',max_length=100)
    MobileNumber    =   models.CharField(("Mobile Number"), default='8766518297',max_length=10)
    Dept= [
        ('Tahasildar', 'Tahasildar'),
        ('CollectorOffice', 'Collector Office'),
        ]
    RecFromDept =   models.CharField(("Received From Department"),max_length=20, choices=Dept)
    priority= [
        ('1Day', '1Day'),
        ('2Day', '2Day'),
        ('3Day', '3Day')
        ]
    Priority        =   models.CharField(("Priority"),max_length=20, choices=priority)
    docsAttch   =   models.FileField(("Attached Documents"), upload_to='documents', max_length=100, null=True , blank=True)
    Desk_id         =   models.CharField(("Desk_id"),max_length=20)
    users= [
        ('user-1', 'user-1'),
        ('user-2', 'user-2'),
        ('user-3', 'user-3'),
        ('user-4', 'user-4')
        ]
    users     =   models.CharField((''),max_length=20, choices=users)
    user_id         =   models.CharField(('user_id'),default='0000000',max_length=20)
    Status      =   models.CharField(max_length=20, default='Unseen')




class TicketPurchaseInformation(models.Model):
    TicketName  =   models.CharField(max_length=50)
    Quantity    =   models.IntegerField()
    Ammount     =   models.IntegerField()
    PurchaseDate    =   models.DateField()


