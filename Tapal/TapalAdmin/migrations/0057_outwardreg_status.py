# Generated by Django 3.0.6 on 2020-07-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0056_remove_outwardreg_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='outwardreg',
            name='Status',
            field=models.BooleanField(default=True),
        ),
    ]
