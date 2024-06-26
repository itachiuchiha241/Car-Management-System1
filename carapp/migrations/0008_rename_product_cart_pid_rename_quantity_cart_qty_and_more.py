# Generated by Django 5.0.1 on 2024-03-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0007_remove_product_product_image_product_carimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='quantity',
            new_name='qty',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='pid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='quantity',
            new_name='qty',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='carimage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_details',
        ),
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Toyota'), (2, 'ford'), (3, 'BMW'), (4, 'Mercedes')], default=1, verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pdetails',
            field=models.CharField(default=1, max_length=1000, verbose_name='Product Details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
