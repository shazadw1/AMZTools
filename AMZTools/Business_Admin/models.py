from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from numpy import blackman


"""Company_related address"""


class AddressModel(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, blank=True, null=True)
    street1 = models.CharField(max_length=200, help_text='Enter street address 1')
    street2 = models.CharField(max_length=200, blank=True, help_text='Enter street address 2')
    area = models.CharField(max_length=200, blank=True, help_text='Enter area')
    city = models.CharField(max_length=200, help_text='Enter city')
    state = models.CharField(max_length=200, help_text='Enter state')
    country = models.CharField(max_length=200, help_text='Enter country')
    registered_address = models.BooleanField(help_text='Enter registered address')
    trading_address = models.BooleanField(help_text='Enter trading address')
    directors_address = models.BooleanField(help_text='Enter director address')
    my_bank_address = models.BooleanField(help_text='Select as Bank address', blank=True, default=False)


"""Company Model added by business admin"""


class CompanyModel(models.Model):
    business_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True, help_text='Enter Company Name')
    registration_number = models.BigIntegerField(blank=True, help_text='Enter company registration number')
    registered_address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True, related_name='reg_address')
    auth_code = models.BigIntegerField(blank=True, help_text='Enter Authentication Code')
    trading_address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True, related_name='trade_address')
    directors_name1 = models.CharField(max_length=100, blank=True, help_text='Enter Directore Name')
    directors_address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True, related_name='director_address')
    directors_name2 = models.CharField(max_length=100, blank=True, help_text='Enter Director name 2')
    directors_address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True, related_name='director_address2')
    certi_incorp = models.FileField(upload_to='incorp_certificates', blank=True, help_text='Upload a copy of certificate incorpation')


# to decide whether the given address is what of boolean field


"""Bank details related to company"""


class BankDetails(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    bank_name = models.CharField(max_length=200)
    sort_code = models.BigIntegerField(null=True)
    account_number = models.BigIntegerField(null=True)
    iban = models.CharField(max_length=20)
    swift_code = models.CharField(max_length=20)
    banks_address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True, related_name='bank_address')


"""Markets details related to company"""


class Markets(models.Model):
    name = models.CharField(max_length=200)
  


"""Brands details related to company"""


class Brands(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    brand_name = models.CharField(max_length=200)


class TradeMark(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=True, null=True)
    market = models.ForeignKey(Markets, on_delete=models.CASCADE, blank=True, null=True)
    trade_mark = models.CharField(max_length=200, blank=True)



# one user can have linked to more than one business admin
