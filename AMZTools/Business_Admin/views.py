from django.shortcuts import render
from django.views import View
from . forms import *
from django.http import HttpResponse
# Create your views here.


class CompanyView(View):
    def get(self, request):
        data = {
        'company_form':CompanyForm(),
        'address_form':AddressForm(),

        }
        return render(request, 'business_admin/company.html', data)


class AddressView(View):
    def get(self, request):
        address_form = AddressForm()
        return render(request, 'business_admin/address.html', {'form':address_form})

    def post(self, request):
        return HttpResponse("yes done")
