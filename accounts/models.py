from django.db import models
from django.contrib import auth

#super user credentials
#admin@gmail.com --> Admin12345

#inherit base manager, add create_user, create_superuser
class UserManager(auth.models.BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            #Normalize the email address by lowercasing the domain part of it.
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    #creating superuser
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#overriding default auth user, inheriting from AbstractBaseUser
class User(auth.models.AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=25)
    #needed for AuthenticationForm
    is_active = models.BooleanField(default=True)
    #superuser fields
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    object = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True
