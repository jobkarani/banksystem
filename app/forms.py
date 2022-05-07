from django import forms
from .models import *

class createBankAccForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'