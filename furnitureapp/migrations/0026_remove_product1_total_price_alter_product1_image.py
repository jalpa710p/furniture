# Generated by Django 5.0.4 on 2024-06-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0025_product1_quantity_product1_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product1',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='product1',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product1/'),
        ),
    ]