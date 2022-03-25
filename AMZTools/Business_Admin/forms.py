from cProfile import label
import imp
from pydoc import text
from random import choices
from secrets import choice
from tkinter import Label
from tkinter.ttk import LabelFrame
from click import option
from django.forms import ModelForm
from . models import *
from django import forms


# filter out request.user in ModelChoiceField for address
    

class CompanyForm(ModelForm):
    registered_address = forms.ModelChoiceField(
        queryset=Address.objects.filter(registered_address=True),
        widget=forms.Select,
        help_text = 'Select Registered Address'
    )

    trading_address = forms.ModelChoiceField(
        queryset=Address.objects.filter(trading_address=True),
        widget=forms.Select,
        help_text = 'Select Trading Address'
    )

    director1_address = forms.ModelChoiceField(
        queryset=Address.objects.filter(directors_address=True),
        widget=forms.Select,
        help_text = 'Select Director 1 Address'
    )

    director2_address = forms.ModelChoiceField(
        queryset=Address.objects.filter(directors_address=True),
        widget=forms.Select,
        help_text = 'Select Director 2 Address'
    )

    class Meta:
        model = Company
        exclude = ['business_admin']
             

class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['user']


class BankForm(ModelForm):
    class Meta:
        model = BankDetails
        fields = '__all__'
