from django import forms
from django_countries.fields import CountryField
#django-countries for dealing with countries, add to installed apps,
#pip freeze > requirements.txt

#django-crispy-forms

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite'
    }))
    country = CountryField(blank_label='Choose...').formfield()
    zip = forms.CharField()
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
