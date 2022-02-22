from django.shortcuts import render
from django.views import View
from . forms import *
from django.http import HttpResponse
# Create your views here.


class AddressView(View):
    def get(self, request):
        address_form = AddressForm()
        return render(request, 'address/address.html', {'form':address_form})

    def post(self, request):
        return HttpResponse("yes done")
