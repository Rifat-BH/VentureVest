# Generated by Django 5.0.4 on 2024-05-06 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0017_merge_20240420_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagedb',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 20, 26, 27, 569254)),
        ),
        migrations.AlterField(
            model_name='messagenofity',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 20, 26, 27, 569254)),
        ),
    ]