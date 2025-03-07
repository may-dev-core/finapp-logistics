# Generated by Django 3.0.7 on 2020-06-19 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20200615_1727'),
        ('apps_settings', '0010_auto_20200619_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceOfIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_of_income', models.CharField(max_length=20, unique=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyProfile')),
            ],
        ),
    ]
