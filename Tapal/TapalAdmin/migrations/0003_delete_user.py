# Generated by Django 3.0.6 on 2020-05-29 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]