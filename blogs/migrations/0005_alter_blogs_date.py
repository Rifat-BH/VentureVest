# Generated by Django 4.1.7 on 2023-04-28 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blogs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 16, 1, 5, 994516)),
        ),
    ]
