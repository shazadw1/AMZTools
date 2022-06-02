from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from . forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import Permission
from .models import *
from django.core.mail import send_mail
from Prod_Validator.tasks import *
from Business_Admin.models import BrandToMarket, PermissionToStaff
from django.core.paginator import Paginator


# form displayed for filling ManualValidator model


class ManualValidationView(View):
    def get(self, request, trade_mark, permission_to_staff_id):
        a=PermissionToStaff.objects.get(id=permission_to_staff_id)
        data = {
            'my_modules':a.staff_modules.split(','),
            'form': ManualValidatorForm(),
            'manual_validator':ManualValidator.objects.filter(brand=BrandToMarket.objects.get(trade_mark=trade_mark)).values('keyword_auto_validate','id')
        }
        return render(request, "product_validator/manual_validator.html", data)

    
    def post(self,request, trade_mark, permission_to_staff_id):
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
    def get(self, request, trade_mark, permission_to_staff_id, mv_pk):
        a=PermissionToStaff.objects.get(id=permission_to_staff_id)
        mv = ManualValidator.objects.get(id=mv_pk)
        head = ManualValidatorHead.objects.get(keyword=mv)
        contact_list = ManualValidatorData.objects.filter(head=head)
        paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'filtering_condition': ManualValidatorDataFilter.objects.filter(mv=mv),
            'my_modules':a.staff_modules.split(','),
            'form': ManualValidatorForm(),
            'manual_validator_head': head,
            'page_obj': page_obj
        }
        return render(request, "product_validator/manual_validator_data.html", data)

    def post(self, request, trade_mark, permission_to_staff_id, mv_pk):
        mv = ManualValidator.objects.get(id=mv_pk)
        if ManualValidatorDataFilter.objects.filter(mv=mv).exists():
            ManualValidatorDataFilter.objects.filter(mv=mv).delete()

        filess = '/home/rutujakadam/AMZTools-main/AMZTools/'+mv.cerebro.url
        mv_f=ManualValidatorDataFilter.objects.create(mv=mv, min_sv=request.POST['min_sv'], min_relavency=request.POST['min_rel'], max_rank=request.POST['min_rank'])
        filter_data.delay(filess, request.POST['min_sv'], request.POST['min_rel'], request.POST['min_rank'], mv_f.id, mv_pk)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


# the original cerebro file data that was saved in model manual_validator_data is filtered with min_sv, min_rev and max_rank


class ManualValidatorFilterView(View):

    def get(self, request, trade_mark, permission_to_staff_id, mv_pk, filtered_condition_id):
        contact_list = ManualValidatorFilteredData.objects.filter(mv_filtered_result__filter__id=filtered_condition_id)
        paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        result = ManualValidatorDataFilterResult.objects.get(filter__id=filtered_condition_id)
        a=PermissionToStaff.objects.get(id=permission_to_staff_id)
        data = {
            'my_modules':a.staff_modules.split(','),
            'form': ManualValidatorForm(),
            'manual_validator_head': ManualValidatorHead.objects.get(keyword__id=mv_pk),
            'page_obj': page_obj,
            'top_ten':list(eval(result.top_10_sv)),
            'top_ten_percent':list(eval(result.top_10percent_sv)),
            'top_thirty':list(eval(result.top_30_sv)),
            'top_thirty_percent':list(eval(result.top_30percent_sv)),
        }
        return render(request,"product_validator/manual_validator_filter_data.html", data)
