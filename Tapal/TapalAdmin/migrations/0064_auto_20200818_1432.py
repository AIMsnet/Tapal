# Generated by Django 3.0.8 on 2020-08-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0063_auto_20200818_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(default='Dept1', max_length=125, unique=True, verbose_name='Department Name'),
        ),
    ]
