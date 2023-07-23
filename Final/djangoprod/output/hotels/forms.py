from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from .models import *
class addFormHotel(forms.Form):

    hotelplace = forms.CharField(label='где надо отель', widget=forms.TextInput(attrs={
        'size': '40',
        'name': "product",
        'id': "product",

            }
        )
    )

    data_incoming = forms.DateField(
        label='с кого числа надо',
        widget=DateInput(
            attrs={
                'type': 'date',
            }
        )
    )

    data_outcomming = forms.DateField(
        label='по какое число',
        widget=DateInput(
            attrs={
                'type': 'date',
            }
        )
    )