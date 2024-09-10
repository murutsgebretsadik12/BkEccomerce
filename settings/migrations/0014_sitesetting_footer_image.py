# Generated by Django 3.1.2 on 2022-05-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_auto_20220522_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='footer_image',
            field=models.ImageField(blank=True, help_text="Please use our recommended dimensions: width='978' height='533'", max_length=1000, null=True, upload_to='site_logo/imgs/', verbose_name='Footer Image'),
        ),
    ]
