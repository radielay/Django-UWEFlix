# Generated by Django 4.0.3 on 2022-03-25 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0011_alter_carddetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetails',
            name='date',
            field=models.DateField(default='Example: 01/01/2022'),
        ),
    ]