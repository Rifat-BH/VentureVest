# Generated by Django 4.1.7 on 2023-04-28 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_alter_commentnofity_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentnofity',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 21, 42, 58, 341416)),
        ),
        migrations.AlterField(
            model_name='communitycomment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 21, 42, 58, 340415)),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 28, 21, 42, 58, 340415)),
        ),
    ]
