from django import forms
from django.forms.fields import CharField


class CheckoutForm(forms.Form):
    """Django formos klasė, kuri yra naudojama kuriant formą, skirtą rinkti informaciją iš
     vartotojo apsipirkimo metu.
     Ji paveldi iš "forms.Form" klasės, kuri yra įtraukta į Django"""
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    zipcode = forms.CharField(max_length=255)
    place = forms.CharField(max_length=255)
    stripe_token = forms.CharField(max_length=255)