# Generated by Django 3.0.6 on 2020-07-08 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0055_inwardreg_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outwardreg',
            name='Status',
        ),
    ]
