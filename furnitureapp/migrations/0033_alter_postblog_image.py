# Generated by Django 5.0.4 on 2024-07-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0032_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='image',
            field=models.ImageField(upload_to='post_blogs/'),
        ),
    ]
