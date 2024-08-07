# Generated by Django 5.0.4 on 2024-06-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0013_remove_testimonial_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='post_images/')),
            ],
        ),
    ]
