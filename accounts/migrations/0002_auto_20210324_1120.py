# Generated by Django 3.1.6 on 2021-03-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Profilephoto',
            field=models.ImageField(blank=True, upload_to='profileimages/'),
        ),
    ]
