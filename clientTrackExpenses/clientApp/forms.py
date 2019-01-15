from django import forms

class ClientExpenseForm(forms.Form):

    title = forms.CharField()
    amount = forms.IntegerField()
    currency = forms.CharField()
    description = forms.CharField()

