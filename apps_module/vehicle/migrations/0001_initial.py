# Generated by Django 3.0.7 on 2020-06-15 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_code', models.CharField(max_length=100)),
                ('vehicle_registration_no', models.CharField(max_length=20, unique=True)),
                ('vehicle_type', models.CharField(max_length=20)),
                ('vehicle_manufacturer', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
                ('vehicle_color', models.CharField(max_length=20)),
                ('vehicle_fuel_type', models.CharField(max_length=20)),
                ('vehicle_purpose', models.CharField(max_length=20)),
                ('vehicle_status', models.CharField(max_length=20)),
                ('vehicle_passenger_limit', models.IntegerField(max_length=100)),
                ('vehicle_cargo_limit', models.CharField(max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyProfile')),
            ],
        ),
    ]
