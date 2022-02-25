from django.urls import path
from . views import *

urlpatterns = [
    path('', CompanyView.as_view(), name='company_view'),
    path('address', AddressView.as_view(), name='address_view')
]
