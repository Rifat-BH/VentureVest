# Generated by Django 4.1.7 on 2023-04-28 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blogs_date_alter_blogs_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 14, 53, 45, 278538)),
        ),
    ]
