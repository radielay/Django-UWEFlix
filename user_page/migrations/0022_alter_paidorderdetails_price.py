# Generated by Django 4.0.4 on 2022-05-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0021_rename_usename_paidorderdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidorderdetails',
            name='price',
            field=models.FloatField(default=3),
        ),
    ]
