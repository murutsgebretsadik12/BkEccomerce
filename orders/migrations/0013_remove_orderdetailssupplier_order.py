# Generated by Django 3.2.12 on 2022-03-18 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_orderdetailssupplier_order_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetailssupplier',
            name='order',
        ),
    ]
