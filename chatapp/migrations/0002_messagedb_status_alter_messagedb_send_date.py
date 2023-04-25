# Generated by Django 4.1.7 on 2023-04-20 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagedb',
            name='status',
            field=models.CharField(default='unseen', max_length=7),
        ),
        migrations.AlterField(
            model_name='messagedb',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 22, 45, 45, 515263)),
        ),
    ]