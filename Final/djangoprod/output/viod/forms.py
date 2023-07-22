from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from .models import *


class addForm(forms.Form):
    flight_date = forms.DateField(
        label='Когда летим',
        widget=DateInput(
            attrs={
                'type': 'date',
            }
        )
    )

    flight_date_reverse = forms.DateField(
        label='Когда обратно',
        widget=DateInput(
            attrs={
                'type': 'date',
            }
        )
    )

    flyfromcity = forms.CharField(widget=forms.TextInput(attrs={
        'size': '40',
        'name': "product",
        'id': "product",

    }))

    flytocity = forms.CharField(widget=forms.TextInput(attrs={
        'size': '40',
        'name': "product2",
        'id': "product2",


    }))



    cabine = forms.ChoiceField(label='ТИП МЕСТА', choices=Product.grade_list, widget=forms.Select(attrs={'class': 'regDropDown'}))



class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass
