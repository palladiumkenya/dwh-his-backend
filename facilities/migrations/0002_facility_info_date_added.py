# Generated by Django 4.0.1 on 2022-03-25 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility_info',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
