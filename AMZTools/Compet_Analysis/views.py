from django.shortcuts import render
# from django.http.response import JsonResponse
from django.views import View
from . forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
# from django.contrib.auth.models import Permission
from .models import *
# from django.core.mail import send_mail
from .tasks import *
from Business_Admin.models import BrandToMarket, PermissionToStaff
from django.core.paginator import Paginator


# form displayed for filling CompAnalysis model


class AddCompAnalysisView(View):
    def get(self, request, trade_mark, permission_to_staff_id):
        a=PermissionToStaff.objects.get(id=permission_to_staff_id)
        data = {
            'my_modules':a.staff_modules.split(','),
            'form': Comp_Analysis_basic_dataForm(),
            'manual_validator':Comp_Analysis_basic_data.objects.filter(brand=BrandToMarket.objects.get(trade_mark=trade_mark)).values('keyword_auto_validate','id')
        }
        return render(request, "compt_analy/manual_validator.html", data)

    
    def post(self,request, trade_mark, permission_to_staff_id):
        formss = Comp_Analysis_basic_dataForm(request.POST, request.FILES)
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


# cerebro excel sheet uploaded in CompAnalysis model extracted in CompAnalysisData model displayed according to keyword saved in CompAnalysis model
# in post method we will be filtering out the data saved in CompAnalysisData model on basis of min SV, min density


class CompAnalysisDataView(View):
    def get(self, request, trade_mark, permission_to_staff_id, mv_pk):
        a=PermissionToStaff.objects.get(id=permission_to_staff_id)
        mv = Comp_Analysis_basic_data.objects.get(id=mv_pk)
        head = Comp_Analysis_KW_Cerebro_Data_Head.objects.get(keyword=mv)
        contact_list = Comp_Analysis_KW_Cerebro_Data.objects.filter(head=head)
        paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'filtering_condition': Comp_Analysis_Data_Filter.objects.filter(mv=mv),
            'my_modules':a.staff_modules.split(','),
            'form': Comp_Analysis_basic_dataForm(),
            'manual_validator_head': head,
            'page_obj': page_obj
        }
        return render(request, "compt_analy/manual_validator_data.html", data)

    def post(self, request, trade_mark, permission_to_staff_id, mv_pk):
        mv = Comp_Analysis_basic_data.objects.get(id=mv_pk)
        head = Comp_Analysis_KW_Cerebro_Data_Head.objects.get(keyword=mv)
        if Comp_Analysis_Data_Filter.objects.filter(mv=mv).exists():
            Comp_Analysis_Data_Filter.objects.filter(mv=mv).delete()

        filess = '/home/rutujakadam/AMZTools-main/AMZTools/'+head.excel_file.url
        mv_f=Comp_Analysis_Data_Filter.objects.create(mv=mv, min_sv=request.POST['min_sv'], min_relavency=request.POST['min_rel'], max_rank=request.POST['min_rank'])
        filter_data.delay(filess, request.POST['min_sv'], request.POST['min_rel'], request.POST['min_rank'], mv_f.id, mv_pk)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


# the original cerebro file data that was saved in model manual_validator_data is filtered with min_sv, min_rev and max_rank


class CompAnalysisFilterView(View):

    def get(self, request, trade_mark, permission_to_staff_id, mv_pk, filtered_condition_id):
        contact_list = Comp_Analysis_Filtered_Data.objects.filter(mv_filtered_result__filter__id=filtered_condition_id)
        paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        result = Comp_Analysis_Data_FilterResult.objects.get(filter__id=filtered_condition_id)
        a=PermissionToStaff.objects.get(id=permission_to_staff_id)
        data = {
            'trade_mark':trade_mark, 'permission_to_staff_id':permission_to_staff_id, 'filtered_condition_id':filtered_condition_id,
            'my_modules':a.staff_modules.split(','),
            'form': Comp_Analysis_basic_dataForm(),
            'manual_validator_head': Comp_Analysis_KW_Cerebro_Data_Head.objects.get(keyword__id=mv_pk),
            'page_obj': page_obj,
            'top_ten':list(eval(result.top_10_sv)),
            'top_ten_percent':list(eval(result.top_10percent_sv)),
            'top_thirty':list(eval(result.top_30_sv)),
            'top_thirty_percent':list(eval(result.top_30percent_sv)),
            # 'top_3':list(eval(result.top_3)),
            'total_search_volume':result.search_volume_total,
            'total_phrase': result.total_phrase
        }
        return render(request,"compt_analy/manual_validator_filter_data.html", data)


class CompAnalysisMasterView(View):
    def get(self, request,trade_mark, permission_to_staff_id, filtered_condition_id):
        master_table.delay(filtered_condition_id)
        return render(request, "compt_analy/master.html")
