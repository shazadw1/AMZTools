from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from . forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import Permission
from .models import *
from django.core.mail import send_mail
from Prod_Validator.tasks import test_func
from Business_Admin.models import BrandToMarket


# form displayed for filling ManualValidator model


class ManualValidationView(View):
    def get(self, request, trade_mark, ppk):
        data = {
            'form': ManualValidatorForm(),
            'manual_validator':ManualValidator.objects.filter(brand=BrandToMarket.objects.get(trade_mark=trade_mark)).values('keyword_auto_validate','id')
        }
        return render(request, "product_validator/manual_validator.html", data)

    
    def post(self,request, trade_mark, ppk):
        formss = ManualValidatorForm(request.POST, request.FILES)
        if formss.is_valid():
            a = formss.save()
            a.brand = BrandToMarket.objects.get(trade_mark=trade_mark)
            a.save()
            filesss = '/home/rutujakadam/AMZTools-main/AMZTools/'+a.cerebro.url
            test_func.delay(filesss, a.id)
            messages.success(request, "Data saved successfully !!Please wait for 1 minute to save cerebro file data")
        else:
            messages.error(request, "Please fill the form correctly.")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


# cerebro excel sheet uploaded in ManualValidator model extracted in ManualValidatorData model displayed according to keyword saved in ManualValidator model
# in post method we will be filtering out the data saved in ManualValidatorData model on basis of min SV, min density


class ManualValidationDataView(View):
    def get(self, request, trade_mark, ppk, mv_pk):
        head = ManualValidatorHead.objects.get(keyword=ManualValidator.objects.get(id=mv_pk))
        data = {
            'manual_validator_head': head,
            'manual_validator_data': ManualValidatorData.objects.filter(head=head)
        }
        return render(request, "product_validator/manual_validator_data.html", data)


