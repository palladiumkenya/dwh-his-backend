# Generated by Django 4.0.1 on 2022-04-20 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0007_alter_edited_facility_info_date_edited_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='edited_facility_info',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='edited_facility_info',
            name='date_edited',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 12, 9, 42, 162473), null=True),
        ),
        migrations.AlterField(
            model_name='facility_info',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 12, 9, 42, 162473), null=True),
        ),
    ]
