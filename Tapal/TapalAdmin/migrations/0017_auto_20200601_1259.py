# Generated by Django 3.0.6 on 2020-06-01 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0016_auto_20200601_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='desc',
            new_name='desk_id',
        ),
    ]