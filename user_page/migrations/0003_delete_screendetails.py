# Generated by Django 4.0.3 on 2022-03-24 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0002_alter_filmdetails_id_alter_screendetails_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScreenDetails',
        ),
    ]
