# Generated by Django 3.2.12 on 2022-02-08 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0015_alter_product_prdslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='product'),
        ),
    ]
