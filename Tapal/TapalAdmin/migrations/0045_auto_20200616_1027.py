# Generated by Django 3.0.6 on 2020-06-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0044_outwardreg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outwardreg',
            name='InwardId',
            field=models.IntegerField(null=True, verbose_name='Inward ID'),
        ),
    ]
