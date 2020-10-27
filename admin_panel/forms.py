from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'password1', 'password2', 'organization', 'inn', 'address', 'okpo']