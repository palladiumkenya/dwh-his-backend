# Generated by Django 4.0.1 on 2022-02-18 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0010_il_info_webadt_pharmacy2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='il_info',
            name='webADT_pharmacy2',
        ),
        migrations.RemoveField(
            model_name='il_info',
            name='webADT_registration2',
        ),
        migrations.AlterField(
            model_name='il_info',
            name='webADT_pharmacy',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='il_info',
            name='webADT_registration',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]