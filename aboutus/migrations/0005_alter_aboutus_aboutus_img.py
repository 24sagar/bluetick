# Generated by Django 5.0 on 2024-01-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0004_alter_aboutus_aboutus_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='aboutus_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='about/'),
        ),
    ]
