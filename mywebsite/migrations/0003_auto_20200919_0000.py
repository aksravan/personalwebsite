# Generated by Django 3.1.1 on 2020-09-18 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_auto_20200918_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ended',
            field=models.DateField(default=datetime.datetime(2020, 9, 18, 18, 30, 48, 65792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='started',
            field=models.DateField(default=datetime.datetime(2020, 9, 18, 18, 30, 48, 65792, tzinfo=utc)),
        ),
    ]