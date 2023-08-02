from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput


class addformorderhotel(forms.Form):
    name = forms.CharField(required=True,label='ФИО')
    phone = forms.CharField(required=True,label='номер телефона')
    address = forms.CharField(required=True,label='адресс')
    email = forms.CharField(required=True,label='e-mail доставки')
    bankcard = forms.CharField(required=True,label='номер карты для оплаты')
    cvcode = forms.CharField(required=True, label='cv code (3 знака сзади карты)')

    
