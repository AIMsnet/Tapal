from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here
# class User(AbstractUser):
#     mobile_no   =   models.BigIntegerField()
#     employee_id      =   models.CharField(max_length=50)
#     role        =   models.CharField(max_length=50)
#     designation =   models.CharField(max_length=50)


class InwardRegistry(models.Model):
    #InwardNumber     =  models.AutoField(null= False)
    ReferenceNumber  =  models.IntegerField(null=False)
    ReferenceRecievedDate   =   models.DateField()
    LatterDetails   =   models.CharField(max_length=150, null=False)
    EmailId =   models.EmailField(max_length=254)
    Address =   models.CharField(max_length=200)
    TYPE_OF_REF= [
        ('Local', 'Local'),
        ('Govt', 'Govt'),
        ]
    ReferenceType = models.CharField(max_length=10, choices=TYPE_OF_REF)
    ReferenceDate   =    models.DateField()
    RecievedFrom    =   models.CharField(max_length=100)
    MobileNumber    =   models.CharField(max_length=10)
    TYPE= [
        ('Tahasildar', 'Tahasildar'),
        ('CollectorOffice', 'Collector Office'),
        ]
    TypeOfReference =   models.CharField(max_length=20, choices=TYPE)
    priority= [
        ('1Day', '1Day'),
        ('2Day', '2Day'),
        ('3Day', '3Day')
        ]
    Priority        =   models.CharField(max_length=20, choices=priority)
    AttachedDocuments   =   models.FileField(upload_to=None, max_length=100)



class TicketPurchaseInformation(models.Model):
    TicketName  =   models.CharField(max_length=50)
    Quantity    =   models.IntegerField()
    Ammount     =   models.IntegerField()
    PurchaseDate    =   models.DateField()


