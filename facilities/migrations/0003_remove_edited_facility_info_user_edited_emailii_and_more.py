# Generated by Django 4.0.1 on 2022-03-15 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0002_remove_edited_facility_info_user_edited_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edited_facility_info',
            name='user_edited_emailii',
        ),
        migrations.RemoveField(
            model_name='edited_facility_info',
            name='user_edited_nameii',
        ),
    ]