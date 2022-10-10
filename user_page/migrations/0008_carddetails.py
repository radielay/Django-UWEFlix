# Generated by Django 4.0.3 on 2022-03-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0007_alter_showingdetails_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=19)),
                ('date', models.DateField(default=1)),
            ],
            options={
                'db_table': 'Card_Details',
            },
        ),
    ]
