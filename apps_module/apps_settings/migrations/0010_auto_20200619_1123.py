# Generated by Django 3.0.7 on 2020-06-19 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_settings', '0009_typeofexpense'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeofexpense',
            old_name='type_expense',
            new_name='type_of_expense',
        ),
    ]