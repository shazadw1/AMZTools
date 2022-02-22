from django.urls import path
from . views import *

urlpatterns = [
   path('sign-up', SignupView.as_view(), name='signup'),
   path('sign-in', SigninView.as_view(), name='sign-in')
]
