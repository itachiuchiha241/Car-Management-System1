# Generated by Django 5.0.1 on 2024-03-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0008_rename_product_cart_pid_rename_quantity_cart_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[('Touota', 'Toyota'), ('ford', 'ford'), ('BMW', 'BMW'), ('Mercedes', 'Mercedes')], verbose_name='Category'),
        ),
    ]
