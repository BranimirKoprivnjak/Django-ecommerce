from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from . import models

class UserCreateForm(UserCreationForm):
    class Meta:
        #model form inherits max_length from model
        #https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#modelform
        model = get_user_model()
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #removes default help_text
        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        #self.fields['email'].widget.attrs['class'] = 'test'
        #self.fields['email'].widget.attrs.update({'class': 'test'})

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password confirmation'


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #AuthenticationForm -> username(email), password
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
