# Generated by Django 4.0.1 on 2022-04-20 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0008_edited_facility_info_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility_info',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='edited_facility_info',
            name='date_edited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 23, 10, 54, 29637), null=True),
        ),
        migrations.AlterField(
            model_name='facility_info',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 23, 10, 54, 29637), null=True),
        ),
    ]