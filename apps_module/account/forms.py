from django import forms
from django.contrib.auth.models import User
from .models import Income, Expenses


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ["date_of_income",
                  "vehicle",
                  "amount",
                  "source_of_income",
                  "income_description", ]
    date_of_income = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', )
    )

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ["date_of_expense",
                  "vehicle",
                  "amount",
                  "type_of_expenditure",
                  "expenditure_description",
                  "receipt_number", ]
    date_of_expense = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', )
    )
