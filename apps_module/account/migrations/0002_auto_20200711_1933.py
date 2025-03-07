# Generated by Django 3.0.7 on 2020-07-11 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20200615_1727'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.CompanyProfile'),
        ),
        migrations.AddField(
            model_name='income',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.CompanyProfile'),
        ),
    ]
