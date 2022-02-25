import imp
from django.forms import ModelForm
from . models import *
    

class CompanyForm(ModelForm):
    class Meta:
        model = CompanyModel
        exclude = ['business_admin']



class AddressForm(ModelForm):
    class Meta:
        model = AddressModel
        fields = '__all__'
