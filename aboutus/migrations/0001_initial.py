# Generated by Django 5.0 on 2024-01-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutus_img', models.ImageField(upload_to='')),
                ('aboutus_dec', models.TextField()),
                ('aboutus_title', models.CharField(max_length=50)),
            ],
        ),
    ]