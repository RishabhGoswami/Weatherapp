from django import forms

class PriceForm(forms.Form):
    city=forms.CharField()