# Generated by Django 5.0 on 2024-01-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_alter_aboutus_aboutus_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='aboutus_img',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
