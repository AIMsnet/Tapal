# Generated by Django 3.0.6 on 2020-06-01 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0010_auto_20200531_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employee_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
