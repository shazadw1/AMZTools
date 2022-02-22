import imp
from django.forms import ModelForm
from . models import *


class AddressForm(ModelForm):
    class Meta:
        model = AddressModel
        fields = '__all__'
