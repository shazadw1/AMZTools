from django.urls import path
from . views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('company', login_required(CompanyView.as_view()), name='company_view'),
    path('add_company', login_required(CompanyAddView.as_view()), name='company_add_view'),

    path('address', login_required(AddressView.as_view()), name='address_view'),
    path('address/<int:pk>', login_required(AddressEdit.as_view()), name='address_edit'),

    path('brand', login_required(BrandView.as_view()), name='brand_view'),
    path('brand/<int:pk>', login_required(BrandEdit.as_view()), name='brand_edit'),

    path('staffemailcheck', login_required(staffemailcheck), name='staffemailcheck'),
    path('staff', login_required(Staff.as_view()), name='staff'),
    path('staff/<int:pk>', login_required(StaffEdit.as_view()), name='staff_edit'),
    path('delete_staff/<int:pk>', login_required(DeleteStaff.as_view()), name='staff_delete'),
    
    path('<str:trade_marks>/<int:permission_to_staff_id>', login_required(WorkInMarket.as_view()), name='market'),
]
