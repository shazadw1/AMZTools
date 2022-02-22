from django.urls import path
from . views import *

urlpatterns = [
   path('', PlanView.as_view(), name='plans'),
   
]
