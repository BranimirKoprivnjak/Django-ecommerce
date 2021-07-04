from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.http import JsonResponse
from accounts.models import User
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class ValidateEmail(View):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('accounts:signup')

    def get(self, request, *args, **kwargs):
        email = self.request.GET.get('email', None)
        data = {
            'is_taken': User.objects.filter(email__iexact=email).exists()
        }
        if data['is_taken']:
            data['error_message'] = 'A user with this username already exists.'
        return JsonResponse(data)

'''
def validate_username(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)
'''
