# Generated by Django 5.0.4 on 2024-06-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0008_featureimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ContainerImage/')),
            ],
        ),
    ]
