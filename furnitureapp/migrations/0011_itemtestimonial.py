# Generated by Django 5.0.4 on 2024-06-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0010_itemproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
                ('image', models.ImageField(upload_to='ItemTestimonial/')),
            ],
        ),
    ]
