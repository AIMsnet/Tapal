# Generated by Django 3.0.6 on 2020-06-02 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TapalAdmin', '0022_remove_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
