# Generated by Django 3.0.8 on 2020-08-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0064_auto_20200818_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(default='Dept1', max_length=125, verbose_name='Department Name'),
        ),
    ]