# Generated by Django 3.1.2 on 2022-05-06 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_contactinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='Worktime',
            new_name='Work_time',
        ),
    ]
