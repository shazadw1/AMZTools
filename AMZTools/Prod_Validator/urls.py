from django.urls import path
from . views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ManualValidationView.as_view()), name='manual_view'),
    path('<int:mv_pk>', login_required(ManualValidationDataView.as_view()), name='manual_data_view')
]
