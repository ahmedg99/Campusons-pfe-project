# Generated by Django 3.1.6 on 2021-03-15 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0006_board_post_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeLogement', models.CharField(max_length=50)),
                ('NombreChambre', models.IntegerField(max_length=1)),
                ('Surface', models.IntegerField(max_length=10)),
                ('Emplacement', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annonce', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]