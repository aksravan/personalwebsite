# Generated by Django 3.1.1 on 2020-09-18 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ended',
            field=models.DateField(default=datetime.datetime(2020, 9, 18, 16, 46, 47, 250225, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='project',
            name='started',
            field=models.DateField(default=datetime.datetime(2020, 9, 18, 16, 46, 47, 250115, tzinfo=utc)),
        ),
    ]