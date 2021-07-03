from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

User = get_user_model()

class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=True)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
