from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from . forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import Permission
from .models import *
from django.core.mail import send_mail
from Prod_Validator.tasks import test_func

"""**********************************************     Company     **********************************************"""

class CompanyView(View):

    def get(self, request):
        data = {
        'company' : Company.objects.filter(business_admin=request.user),
        'invited_company' : PermissionToStaff.objects.filter(to_staff=request.user),
        'address':Address.objects.filter(user=request.user)
        }
        return render(request, 'business_admin/company_view.html', data)

    def post(self, request, pk):
        Company.objects.get(id=pk).delete()
        messages.success(request, 'Company deleted successfully !!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class CompanyAddView(View):

    def get(self, request):
        data = {
        'company_form':CompanyForm(),
        'address_form':AddressForm(),
        }
        return render(request, 'business_admin/company.html', data)
    
    def post(self, request):
        company = CompanyForm(data=request.POST, files=request.FILES)
        if company.is_valid():
            comp = company.save()
            comp.business_admin = request.user
            comp.save()
            messages.success(request, 'Company added successfully !!')
        else:
            messages.error(request, 'Some data missing !!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


"""**********************************************      Address     **********************************************"""


class AddressView(View):

    def get(self, request):
        data = {'address':Address.objects.filter(user=request.user)}
        return render(request, 'business_admin/address.html', data)

    def post(self, request):
        print(request.POST)
        address = AddressForm(request.POST)
        if address.is_valid():
            address = address.save()
            address.user = request.user
            address.save()
            messages.success(request, "Address added Successfully !!")
            data = {'pk':address.id, 'resp':'Address Added successfully !!'}
        else:
            data = {'resp':'Something went wrong! Please check all fields are filled properly !!'}
        return JsonResponse(data)


class AddressEdit(View):

    def get(self, request, pk):
        Address.objects.filter(id=pk).delete()
        messages.success(request, "Address deleted Successfully !!")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
    def post(self, request, pk):
        address = AddressForm(instance=Address.objects.get(id=pk), data=request.POST)
        if address.is_valid():
            address.save()
            messages.success(request, "Address updated Successfully !!")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])  


"""**********************************************      Brand     **********************************************"""


class BrandView(View):

    def get(self, request):
        data = {
            'brand':BrandToMarket.objects.filter(brand__company__business_admin=request.user),
            'brands':Brands.objects.filter(company__business_admin=request.user),
            'market':Markets.objects.all(),
            'company':Company.objects.filter(business_admin=request.user)
        }
        return render(request, 'business_admin/brands.html', data)
    
    def post(self, request):
        comp = Company.objects.get(id=request.POST['company'])
        market = Markets.objects.get(id=request.POST['market_name'])
        if request.POST['brand_name1'] == '':
            BrandToMarket.objects.create(brand = Brands.objects.get(id=request.POST['brand_name']), market = market, trade_mark = request.POST['trademark'])
        else:
            new_brand = Brands.objects.create(company = comp, brand_name = request.POST['brand_name1'])
            BrandToMarket.objects.create(brand = new_brand, market = market, trade_mark = request.POST['trademark'])
        return HttpResponseRedirect(request.META['HTTP_REFERER'])   


class BrandEdit(View):

    def get(self, request, pk):
        BrandToMarket.objects.filter(id=pk).delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER']) 


"""**********************************************      Staff     **********************************************"""


def staffemailcheck(request):
    email = request.GET.get('email')
    if User.objects.filter(email=email).exists():
        data = {'num':1}
    else:
        data = {'num':2}
    return JsonResponse(data)


class Staff(View):

    def get(self, request):
        data = {
            'brands_in_market' : BrandToMarket.objects.filter(brand__company__business_admin=request.user),
            'permission_staff': PermissionToStaff.objects.filter(brand_to_country__brand__company__business_admin=request.user),
        }
        return render(request, "business_admin/staff.html", data)
    
    def post(self ,request):
        iemail = request.POST.get('email')
        if request.POST.get('brand_to_country') != '':
            if PermissionToStaff.objects.filter(to_staff__email=iemail, brand_to_country__id=request.POST.get('brand_to_country')).exists():
                messages.error(request, "The user is added to this brand already !!")
            else:
                email = User.objects.get(email=iemail)
                brand = BrandToMarket.objects.get(id=request.POST.get('brand_to_country'))
                PermissionToStaff.objects.create(to_staff=email, brand_to_country=brand)
        else:
            send_mail(
                        'Invitation to join website_name',
                        f'Hello, \n I am {request.user.first_name} {request.user.last_name}.\n'+
                        'Please Signup using link  <a href="http://127.0.0.1:8000/user/sign-up">SignUp</a>',
                        request.user.email,
                        [iemail],
                        fail_silently=False,
                    )
            PendingStaff.objects.create(to_staff=iemail)
        return HttpResponseRedirect(request.META['HTTP_REFERER']) 


class StaffEdit(View):

    def get(self, request, pk):
        data = {
            'given_permissions' : PermissionToStaff.objects.get(id=pk),
            'permissions': Permission.objects.all()}
        return render(request, "business_admin/edit_staff.html", data) 
    
    def post(self, request, pk):
        a = request.POST.getlist('staff_permission')
        for i in PermissionToStaff.objects.filter(id=pk):
            i.staff_permission.add(*a)
        return HttpResponseRedirect(request.META['HTTP_REFERER']) 


class DeleteStaff(View):

    def get(self, request, pk):
        PermissionToStaff.objects.filter(id=pk).delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER']) 


"""Working area for workers"""


class WorkInMarket(View):

    def get(self, request, trade_marks, permission_to_staff_id):
        a=PermissionToStaff.objects.get(id=permission_to_staff_id)
        data = {'my_modules':a.staff_modules.split(',')}
        return render(request, 'base/base2.html', data)


import pandas as pd


def display_csv(request):
    df = pd.read_excel('/home/rutujakadam/Downloads/Cerebro.xlsx')
    df = df.loc[:, ~df.columns.isin(['Cerebro IQ Score', 'Search Volume Trend (30 days)','Competing Products','CPR','Sponsored ASINs','Amazon Recommended','Sponsored','Organic','Sponsored Rank (avg)','Sponsored Rank (count)','Amazon Recommended Rank (avg)','Amazon Recommended Rank (count)','Relative Rank','Competitor Rank (avg)','Ranking Competitors (count)','Competitor Performance Score'])]
    dict1 = df.to_html() 
    return render(request, "display_csv.html", {'dict1':dict1})
