# Generated by Django 4.0.1 on 2022-07-26 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mob', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('edt', models.DateField()),
                ('remarks', models.CharField(default=None, max_length=100)),
                ('name', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('sal', models.IntegerField()),
                ('joined_dt', models.DateField()),
                ('timing', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Joined',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_dt', models.DateField()),
                ('total', models.IntegerField()),
                ('first_ins', models.IntegerField()),
                ('first_dt', models.DateField()),
                ('last_ins', models.IntegerField()),
                ('last_dt', models.DateField()),
                ('duration', models.CharField(max_length=20)),
                ('dues', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_dt', models.DateField()),
                ('trainer', models.CharField(max_length=30)),
                ('bname', models.CharField(max_length=40)),
                ('student', models.ManyToManyField(to='home.Joined')),
            ],
        ),
    ]