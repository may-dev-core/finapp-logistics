# Generated by Django 3.0.7 on 2020-06-15 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_settings', '0006_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_settings.Position'),
        ),
    ]
