# Generated by Django 5.0.6 on 2024-06-25 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles/'),
        ),
    ]
