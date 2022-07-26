from django.urls import path
from . views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(AddCompAnalysisView.as_view()), name='comp_view'),
    path('<int:mv_pk>', login_required(CompAnalysisDataView.as_view()), name='comp_data_view'),
    path('<int:mv_pk>/<int:filtered_condition_id>', login_required(CompAnalysisFilterView.as_view()), name='comp_filter_data_view'),
    path('<int:filtered_condition_id>/master', login_required(CompAnalysisMasterView.as_view()), name='comp_master_view')
    ]
