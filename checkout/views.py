from django.shortcuts import render, redirect
from django.views.generic import View
#from django.views.generic.edit import FormView
#from accounts.models import User
from checkout.models import BillingAddress
from checkout.forms import CheckoutForm
from shop.models import Order
#from django.contrib.auth import get_user_model
from . import forms
import paypalrestsdk
# Create your views here.

#order = Order.objects.get(user=self.request.user, ordered=False)
#billing_address = order.billing_address.objects.get()

#FormView, form_valid
class CheckoutView(View):
    def get(self, *args, **kwargs):
        billing_address = BillingAddress.objects.filter(
            order__user = self.request.user, order__ordered = False
        )
        if billing_address.exists():
            form = CheckoutForm(initial={
                'street_address': billing_address[0].street_address,
                'apartment_address': billing_address[0].apartment_address,
                'country': billing_address[0].country,
                'zip': billing_address[0].zip
            })
        else:
            form = CheckoutForm()
        context = {
            'form':form
        }
        return render(self.request, 'checkout/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        order = Order.objects.get(user=self.request.user, ordered=False)
        if form.is_valid():
            street_address = form.cleaned_data.get('street_address')
            apartment_address = form.cleaned_data.get('apartment_address')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            payment_option = form.cleaned_data.get('payment_option')
            billing_address = BillingAddress(
                user=self.request.user,
                street_address=street_address,
                apartment_address=apartment_address,
                country=country,
                zip=zip,
            )
            billing_address.save()
            order.billing_address = billing_address
            order.save()
        return redirect('checkout:payment')

class PaymentView(View):
    def get(self, *args, **kwargs):
        self.request.headers = {
            'Content-Type': 'application/json'
        }
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'total':order.total
        }
        return render(self.request, 'checkout/payment.html', context)
