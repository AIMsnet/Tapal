# Generated by Django 3.0.6 on 2020-06-09 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0035_auto_20200609_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inwardreg',
            name='status',
        ),
    ]
