# Generated by Django 4.1.7 on 2023-04-28 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
        ('backupStartupDB', '0005_applyforfundrising_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='return_profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime(2023, 4, 28, 21, 42, 58, 343417))),
                ('comments', models.CharField(max_length=30)),
                ('inv_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_id', to='auths.auts')),
                ('st_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='st_id', to='auths.auts')),
            ],
        ),
    ]
