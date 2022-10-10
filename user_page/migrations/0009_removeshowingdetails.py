# Generated by Django 4.0.4 on 2022-05-07 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0008_removescreendetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoveShowingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_showing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_page.showingdetails')),
            ],
        ),
    ]
