# Generated by Django 3.0.6 on 2020-07-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0052_auto_20200708_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inwardreg',
            name='Status',
            field=models.BooleanField(default=True),
        ),
    ]
