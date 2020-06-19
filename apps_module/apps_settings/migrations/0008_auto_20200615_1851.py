# Generated by Django 3.0.7 on 2020-06-15 18:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('apps_settings', '0007_auto_20200615_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number_1',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='format +233147258369', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='format +233147258369', max_length=128, null=True, region=None),
        ),
    ]
