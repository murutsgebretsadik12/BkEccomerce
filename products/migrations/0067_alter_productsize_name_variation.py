# Generated by Django 3.2.14 on 2022-10-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0066_productsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='name_variation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name Variation'),
        ),
    ]
