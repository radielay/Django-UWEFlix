# Generated by Django 4.0.4 on 2022-05-09 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_page', '0012_removeuserdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoveStaffDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='club',
            name='Representatives',
        ),
        migrations.RemoveField(
            model_name='club',
            name='Students',
        ),
        migrations.RemoveField(
            model_name='club',
            name='contact_email',
        ),
        migrations.AddField(
            model_name='club',
            name='rep_email',
            field=models.EmailField(default='none', max_length=254),
        ),
        migrations.AddField(
            model_name='club',
            name='rep_name',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.DeleteModel(
            name='Representatives',
        ),
    ]
