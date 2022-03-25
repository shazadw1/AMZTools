from django.shortcuts import render
from django.views import View
from . forms import *
from django.http import HttpResponseRedirect
# Create your views here.


class PlanView(View):
    def get(self, request):
        data = {
            'plans':Package.objects.filter(visible=True).values('name', 'pricing_per_month', 'description'), 
            'limits':Package.objects.filter(visible=True).values_list('company_limit', 'users_limit', 'brands_limit',
                                                        'markets_limit','product_validation_limit',
                                                        'comp_analysis_limit','listings_limit',
                                                        'ppc_generation_limit','ppc_optimization_limit')
        }
        return render(request, 'plans/packages.html', data)

    def post(self, request, plan_pk):
        Business_Admin_Plan.objects.create_or_update(user=request.user, plan=Package.objects.get(id=plan_pk))
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

       