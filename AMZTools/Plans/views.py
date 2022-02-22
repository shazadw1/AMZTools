from django.shortcuts import render
from django.views import View
from . forms import *
from django.http import HttpResponse
# Create your views here.


class PlanView(View):
    def get(self, request):
        address_form = PackageForm()
        data = {
            'form':address_form, 
            'plans':Package.objects.all().values('name', 'pricing_per_month', 'description'), 
            'limits':Package.objects.all().values_list('company_limit', 'users_limit', 'brands_limit',
                                                        'markets_limit','product_validation_limit',
                                                        'comp_analysis_limit','listings_limit',
                                                        'ppc_generation_limit','ppc_optimization_limit')
        }
        return render(request, 'plans/packages.html', data)

    def post(self, request):
        plan_form = PackageForm(request.POST)
        if plan_form.is_valid():
            plan_form.save()
            return HttpResponse("saved !!!")
        else:
            return HttpResponse("not saved")
        