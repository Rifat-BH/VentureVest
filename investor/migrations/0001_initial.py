# Generated by Django 4.1.6 on 2023-03-31 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company_name', models.CharField(max_length=50)),
                ('invest_ammount', models.CharField(max_length=10)),
                ('returen_rate', models.CharField(max_length=5)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.auts')),
            ],
        ),
    ]
