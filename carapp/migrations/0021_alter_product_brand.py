# Generated by Django 5.0.1 on 2024-03-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0020_alter_product_brand_alter_product_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('BMW', 'BMW'), ('Mercedes', 'Mercedes')], max_length=100, verbose_name='Brand'),
        ),
    ]
