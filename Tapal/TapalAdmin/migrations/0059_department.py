# Generated by Django 3.0.8 on 2020-08-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0058_user_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=125)),
                ('dept_phno', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=6)),
            ],
        ),
    ]
