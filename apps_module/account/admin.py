from django.contrib import admin
from .models import Income, Expenses

# Register your models here.
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'date_of_income',
        'vehicle',
        'amount',
        'source_of_income',
        'income_description',
        'date_added',
        'date_updated',
    ]

    class Meta:
        model = Income


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'date_of_expense',
        'vehicle',
        'type_of_expenses',
        'amount',
        'expense_description',
        'receipt_number',
        'date_added',
        'date_updated',
    ]

    class Meta:
        model = Expenses
