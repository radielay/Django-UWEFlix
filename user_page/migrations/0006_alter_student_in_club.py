# Generated by Django 4.0.4 on 2022-05-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0005_student_in_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='in_club',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5),
        ),
    ]
