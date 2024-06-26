# Generated by Django 5.0.1 on 2024-03-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0018_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('BMW', 'BMW'), ('MERCEDES', 'Mercedes')], max_length=50, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[(1, 'SUV'), (2, 'Sedan'), (3, 'Hatchback')], max_length=20, verbose_name='Category'),
        ),
    ]
