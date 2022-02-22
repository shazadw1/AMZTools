from django.urls import path
from . views import *

urlpatterns = [
    path('', AddressView.as_view(), name='address_view')
]
