# Generated by Django 3.0.6 on 2020-06-01 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0012_remove_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='InwardRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReferenceNumber', models.IntegerField(verbose_name='Reference Number')),
                ('ReferenceRecievedDate', models.DateField(default=datetime.datetime.now, verbose_name='Reference Recieved Date')),
                ('LatterDetails', models.CharField(max_length=150, verbose_name='Latter Details')),
                ('EmailId', models.EmailField(max_length=254, verbose_name='E-mail ID')),
                ('Address', models.CharField(max_length=200, verbose_name='Address')),
                ('ReferenceType', models.CharField(choices=[('Local', 'Local'), ('Govt', 'Govt')], max_length=10, verbose_name='Reference Type')),
                ('ReferenceDate', models.DateField(default=datetime.datetime.now, verbose_name='Reference Date')),
                ('RecievedFrom', models.CharField(max_length=100, verbose_name='Recieved From')),
                ('MobileNumber', models.CharField(max_length=10, verbose_name='Mobile Number')),
                ('TypeOfReference', models.CharField(choices=[('Tahasildar', 'Tahasildar'), ('CollectorOffice', 'Collector Office')], max_length=20, verbose_name='Type Of Reference')),
                ('Priority', models.CharField(choices=[('1Day', '1Day'), ('2Day', '2Day'), ('3Day', '3Day')], max_length=20, verbose_name='Priority')),
                ('AttachedDocuments', models.FileField(upload_to=None, verbose_name='Attached Documents')),
            ],
        ),
        migrations.CreateModel(
            name='TicketPurchaseInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketName', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Ammount', models.IntegerField()),
                ('PurchaseDate', models.DateField()),
            ],
        ),
    ]
