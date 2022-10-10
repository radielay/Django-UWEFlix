# Generated by Django 4.0.4 on 2022-05-07 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0009_removeshowingdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoveMovieDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_page.filmdetails')),
            ],
        ),
    ]
