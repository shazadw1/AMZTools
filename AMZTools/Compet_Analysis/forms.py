from django.forms import ModelForm
from . models import *


class Comp_Analysis_basic_dataForm(ModelForm):
    class Meta:
        model = Comp_Analysis_basic_data
        exclude = ['brand', 'xray']
