# Generated by Django 4.0.3 on 2022-03-25 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0010_carddetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetails',
            name='date',
            field=models.DateField(default='01/01/2022'),
        ),
    ]
