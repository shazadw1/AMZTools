from curses.ascii import US
from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


"""Company Model added by business admin"""


class CompanyModel(models.Model):
    business_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True)
    registration_number = models.BigIntegerField(blank=True)
    auth_code = models.BigIntegerField(blank=True)
    directors_name1 = models.CharField(max_length=100, blank=True)
    directors_name2 = models.CharField(max_length=100, blank=True)
    certi_incorp = models.FileField(upload_to='incorp_certificates', blank=True)


"""Company_related address"""


class AddressModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200, blank=True)
    area = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    registered_address = models.BooleanField()
    trading_address = models.BooleanField()
    directors_address = models.BooleanField()

# to decide whether the given address is what of boolean field


"""Bank details related to company"""


class BankDetails(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    bank_name = models.CharField(max_length=200)
    sort_code = models.BigIntegerField(null=True)
    account_number = models.BigIntegerField(null=True)
    iban = models.CharField(max_length=20)
    swift_code = models.CharField(max_length=20)
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200, blank=True)
    area = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


"""Brands details related to company"""


class Brands(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    brand_name = models.CharField(max_length=200)


"""Markets details related to company"""


class Markets(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    trade_mark = models.CharField(max_length=200)



# one user can have linked to more than one business admin
