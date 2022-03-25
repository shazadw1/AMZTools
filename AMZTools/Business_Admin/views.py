from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from httplib2 import Response
from . forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


class CompanyView(View):
    def get(self, request):
        data = {
        'company_form':CompanyForm(),
        'address_form':AddressForm(),
        }
        return render(request, 'business_admin/company.html', data)
    
    def post(self, request):
        company = CompanyForm(request.POST)
        if company.is_valid():
            company.save(business_admin=request.user)
            messages.success(request, 'Company added successfully !!')
        else:
            messages.error(request, 'Some data missing !!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AddressView(View):
    def post(self, request):
        address = AddressForm(request.POST)
        if address.is_valid():
            address.save(user=request.user)
            data = {'resp':address.id}
        else:
            data = {'resp':'Something went wrong! Please save address again !!'}
        return JsonResponse(data)
