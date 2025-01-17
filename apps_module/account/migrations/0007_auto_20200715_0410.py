# Generated by Django 3.0.7 on 2020-07-15 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200715_0406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='expense_description',
            new_name='expenditure_description',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='type_of_expenditure',
            field=models.CharField(blank=True, choices=[('General Servicing', 'General Servicing'), ('Other', 'Other'), ('Fuel', 'Fuel'), ('Repairs', 'Repairs')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='source_of_income',
            field=models.CharField(blank=True, choices=[('Delivery', 'Delivery'), ('Hiring', 'Hiring'), ('Other', 'Other'), ('Transportation', 'Transportation')], max_length=20, null=True),
        ),
    ]
