from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, user_directory_path


class RegistrationForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(required=True, max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'First Name',
                                 }))

    last_name = forms.CharField(required=True, max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last Name',
                                }))

    username = forms.CharField(required=True, max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username',
                               }))

    email = forms.EmailField(required=True, max_length=100,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email',
                             }))
    password1 = forms.CharField(required=True, max_length=100,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password',
                                }))

    password2 = forms.CharField(required=True, max_length=100,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Confirm Password',
                                }))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username',
                               }))

    password = forms.CharField(required=True, max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Password',
                               }))

    remember_me = forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(attrs={
                                         'class': 'form-check-input',
                                         'placeholder': 'Remember Me',
                                     }))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'remember_me')
