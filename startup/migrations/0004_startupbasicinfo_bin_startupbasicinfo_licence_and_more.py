# Generated by Django 4.1.7 on 2023-03-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startupbasicinfo',
            name='bin',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='startupbasicinfo',
            name='licence',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='startupbasicinfo',
            name='vat',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='startupbasicinfo',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]