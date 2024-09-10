# Generated by Django 3.2.12 on 2022-02-03 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20220203_0652'),
        ('products', '0003_auto_20220203_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_maincategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.maincategory', verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_minicategor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.minicategory', verbose_name='Mini Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory', verbose_name='Sub Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_supercategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.supercategory', verbose_name='Super Category'),
        ),
    ]
