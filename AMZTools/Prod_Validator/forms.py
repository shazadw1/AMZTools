from django.forms import ModelForm
from . models import *


class ManualValidatorForm(ModelForm):
    class Meta:
        model = ManualValidator
        exclude = ['brand', 'xray','amazon_choice','magnet']
