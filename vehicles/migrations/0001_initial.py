# Generated by Django 3.1.8 on 2021-04-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('length', models.CharField(max_length=64)),
                ('width', models.CharField(max_length=64)),
                ('hin', models.CharField(max_length=12, verbose_name='HIN')),
                ('current_hours', models.IntegerField()),
                ('service_interval', models.CharField(max_length=128)),
                ('next_service', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField(default=4)),
                ('color', models.CharField(max_length=128)),
                ('vin', models.CharField(max_length=17, verbose_name='VIN')),
                ('current_mileage', models.IntegerField(default=0)),
                ('service_interval', models.CharField(max_length=128)),
                ('next_service', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('bed_length', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=128)),
                ('vin', models.CharField(max_length=17, verbose_name='VIN')),
                ('current_mileage', models.IntegerField(default=0)),
                ('service_interval', models.CharField(max_length=128)),
                ('next_service', models.DateField()),
            ],
        ),
    ]