from django import forms
from .models import Income, Expenses


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["date_of_income",
                  "vehicle",
                  "amount",
                  "source_of_income",
                  "income_description", ]


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ["date_of_expense",
                  "vehicle",
                  "amount",
                  "type_of_expenditure",
                  "expenditure_description",
                  "receipt_number", ]
