# Generated by Django 5.0.4 on 2024-05-06 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_alter_blogs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 20, 26, 27, 573254)),
        ),
    ]