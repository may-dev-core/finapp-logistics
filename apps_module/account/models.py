from django.db import models
from apps_module.vehicle.models import Vehicle
from apps_module.apps_settings.models import TypeOfExpense, SourceOfIncome

# Create your models here.


class Income(models.Model):
    date_of_income = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.FloatField()
    source_of_income = models.ForeignKey(
        SourceOfIncome, on_delete=models.CASCADE)
    income_description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.source_of_income)


class Expenses(models.Model):
    date_of_expense = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type_of_expenses = models.ForeignKey(
        TypeOfExpense, on_delete=models.CASCADE)
    amount = models.FloatField()
    expense_description = models.TextField(blank=True, null=True)
    receipt_number = models.CharField(max_length=20, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.type_of_expenses)
