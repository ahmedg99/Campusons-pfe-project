# Generated by Django 3.1.7 on 2021-03-19 14:26

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_auto_20210318_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='NumTel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]