# Generated by Django 4.0.4 on 2022-05-07 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Club name')),
                ('address', models.CharField(max_length=50, verbose_name='Address: ')),
                ('address2', models.CharField(blank=True, default='', max_length=50, verbose_name='Address 2 (Optional): ')),
                ('city', models.CharField(default='', max_length=30, verbose_name='City: ')),
                ('postcode', models.CharField(default='', max_length=7, verbose_name='Postcode: ')),
                ('contact_number', models.IntegerField()),
                ('landline_number', models.IntegerField(blank=True, null=True)),
                ('contact_email', models.EmailField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilmDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media')),
                ('age_rating', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('date', models.DateField(help_text='Example: 2022-01-01', null=True)),
                ('time', models.TimeField(help_text='Example: 10:30', null=True)),
                ('screen_type', models.CharField(default='2D', max_length=5)),
                ('selected_seats', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveBigIntegerField(default=3)),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='UpcomingFilmDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media')),
                ('age_rating', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'Upcoming_Movies',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('id_number', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('credits', models.PositiveIntegerField(default=0)),
                ('Club', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='user_page.club')),
            ],
        ),
        migrations.CreateModel(
            name='ShowingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Example: 2022-01-01')),
                ('time', models.TimeField(help_text='Example: 10:30')),
                ('Films', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_page.filmdetails')),
            ],
            options={
                'db_table': 'Showings',
            },
        ),
        migrations.CreateModel(
            name='ScreenDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats_available', models.PositiveIntegerField()),
                ('screen_type', models.CharField(choices=[('1', '2D'), ('2', '3D')], default='1', max_length=2)),
                ('Showings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_page.showingdetails')),
            ],
            options={
                'db_table': 'Screens',
            },
        ),
        migrations.CreateModel(
            name='Representatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('Club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_page.club')),
            ],
        ),
        migrations.CreateModel(
            name='RemoveUpcomingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_page.upcomingfilmdetails')),
            ],
        ),
        migrations.CreateModel(
            name='RemoveOrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_page.orderdetails')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='screen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_page.screendetails'),
        ),
        migrations.AddField(
            model_name='club',
            name='Representatives',
            field=models.ManyToManyField(blank=True, to='user_page.representatives'),
        ),
        migrations.AddField(
            model_name='club',
            name='Students',
            field=models.ManyToManyField(blank=True, to='user_page.student'),
        ),
    ]
