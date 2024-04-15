from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):

    class Meta:
        model= User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))