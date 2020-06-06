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
 



class InwardRegistry(models.Model):
    #InwardNumber     =  models.AutoField(null= False)
    ReferenceNumber  =  models.IntegerField(("Reference Number"), null=False)
    ReferenceRecievedDate   =   models.DateField(("Reference Recieved Date"), default=datetime.now)
    LatterDetails   =   models.CharField(("Latter Details"),max_length=150, null=False)
    EmailId =   models.EmailField(("E-mail ID"),max_length=254)
    Address =   models.CharField(("Address"),max_length=200)
    TYPE_OF_REF= [
        ('Local', 'Local'),
        ('Govt', 'Govt'),
        ]
    ReferenceType = models.CharField(("Reference Type"),max_length=10, choices=TYPE_OF_REF)
    ReferenceDate   =    models.DateField(("Reference Date"), default=datetime.now)
    RecievedFrom    =   models.CharField(("Recieved From"),max_length=100)
    MobileNumber    =   models.CharField(("Mobile Number"),max_length=10)
    TYPE= [
        ('Tahasildar', 'Tahasildar'),
        ('CollectorOffice', 'Collector Office'),
        ]
    TypeOfReference =   models.CharField(("Type Of Reference"),max_length=20, choices=TYPE)
    priority= [
        ('1Day', '1Day'),
        ('2Day', '2Day'),
        ('3Day', '3Day')
        ]
    Priority        =   models.CharField(("Priority"),max_length=20, choices=priority)
    AttachedDocuments   =   models.FileField(("Attached Documents"), upload_to='docs', max_length=100)
    Desk_id         =   models.CharField(("Desk_id"),max_length=20)
    Dept= [
        ('user-1', 'user-1'),
        ('user-2', 'user-2'),
        ('user-3', 'user-3'),
        ('user-4', 'user-4')
        ]
    Departments     =   models.CharField((''),max_length=20, choices=Dept)
    user_id         =   models.CharField(('user_id'),default='0000000',max_length=20)


class TicketPurchaseInformation(models.Model):
    TicketName  =   models.CharField(max_length=50)
    Quantity    =   models.IntegerField()
    Ammount     =   models.IntegerField()
    PurchaseDate    =   models.DateField()


