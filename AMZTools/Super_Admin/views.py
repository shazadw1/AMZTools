from re import I
import re
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.
class SignupView(View):
    def get(self, request):        
        return render(request, 'login_system/signup.html')

    def post(self, request):
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, "The email is already registered with us. Please try different Url")
            return redirect('signup')
        else:
            User.objects.create(username=request.POST['email'],email=request.POST['email'], password=request.POST['password'])
            messages.success(request, "You have signed up successfully !!")
            return redirect("sign-in")
        


# Create your views here.
class SigninView(View):
    def get(self, request):        
        return render(request, 'login_system/signin.html')

    def post(self, request):
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if User.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect("address_view")
        else:
            messages.error(request, "Either this mail is not registered with us or email and password does not matches.")
            return redirect("sign-in")
