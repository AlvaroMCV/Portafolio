# Generated by Django 5.0.6 on 2024-06-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
