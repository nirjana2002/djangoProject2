from django import forms

from banks.models import Bank


class BankCreationForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = [
            'name',
            'CEO_name',
            'location',
            'number_of_branches',
            'number_of_employees',
        ]


class BankUpdatationForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = [
            'name',
            'CEO_name',
            'location',
            'number_of_branches',
            'number_of_employees',
        ]