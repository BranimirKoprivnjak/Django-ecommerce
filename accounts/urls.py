from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=forms.UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('ajax/validate_email/', views.ValidateEmail.as_view(), name='validate_email')
]
