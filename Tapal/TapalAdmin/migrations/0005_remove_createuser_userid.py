# Generated by Django 3.0.6 on 2020-05-30 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0004_createuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createuser',
            name='userId',
        ),
    ]