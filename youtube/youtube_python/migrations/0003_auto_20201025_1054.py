# Generated by Django 3.0.10 on 2020-10-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_python', '0002_auto_20201024_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
