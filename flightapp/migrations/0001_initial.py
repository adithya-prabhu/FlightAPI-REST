# Generated by Django 4.1 on 2022-08-17 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNumber', models.CharField(max_length=20)),
                ('operatingcity', models.CharField(max_length=20)),
                ('departurecity', models.CharField(max_length=20)),
                ('arrivalcity', models.CharField(max_length=20)),
                ('dateofdeparture', models.DateField()),
                ('estimatedTimeofDeparture', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('middleName', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightapp.flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightapp.passenger')),
            ],
        ),
    ]