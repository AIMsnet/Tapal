# Generated by Django 3.0.6 on 2020-07-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0054_remove_inwardreg_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='inwardreg',
            name='Status',
            field=models.BooleanField(default=True),
        ),
    ]