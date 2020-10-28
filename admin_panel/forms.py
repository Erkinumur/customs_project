from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class WorkerForm(UserCreationForm):
    organization = forms.CharField(label='Организация', max_length=100)
    phone = forms.CharField(label='Тел.номер', max_length=200)
    passport_id = forms.CharField(label='ID паспорта', max_length=50)
    place = forms.CharField(label='Местоположение', max_length=200)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'organization', 'phone', 'passport_id', 'place']


class DriverForm(UserCreationForm):
    car_number = forms.CharField(label='Номер машины', max_length=50)
    category = forms.CharField(label='Категория',max_length=30)
    car_model = forms.CharField(label='Модель', max_length=100)
    year_of_issue = forms.IntegerField(label='Год выпуска')
    color = forms.CharField(label='Цвет кузова', max_length=100)
    chassis = forms.CharField(label='Шасси', max_length=100)
    body_type = forms.CharField(label='Тип кузова', max_length=100)
    engine_power = forms.CharField(label='Мощность двигаетля', max_length=100)
    engine_type = forms.CharField(label='Тип двигателя', max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2','category', 'car_model', 'year_of_issue', 'color', 'chassis', 'body_type', 'engine_power', 'engine_type']
