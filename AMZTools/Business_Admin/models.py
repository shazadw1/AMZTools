from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User


"""Company_related address"""


class Address(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, blank=True, null=True)
    street1 = models.CharField(max_length=200, help_text='Enter street address 1')
    street2 = models.CharField(max_length=200, blank=True, help_text='Enter street address 2')
    area = models.CharField(max_length=200, blank=True, help_text='Enter area')
    city = models.CharField(max_length=200, help_text='Enter city')
    state = models.CharField(max_length=200, help_text='Enter state')
    country = models.CharField(max_length=200, help_text='Enter country')
    registered_address = models.BooleanField(help_text='Click to select as registered address')
    trading_address = models.BooleanField(help_text='Click to select as trading address')
    directors_address = models.BooleanField(help_text='Click to select as director address')
    my_bank_address = models.BooleanField(help_text='Click to select as Bank address', blank=True, default=False)

    def __str__(self):
        return (self.street1+','+self.street2+'\n'+self.area+','+self.city+','+self.state+','+self.country)


"""Company Model added by business admin"""


class Company(models.Model):
    business_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True, help_text='Enter Company Name')
    registration_number = models.BigIntegerField(blank=True, help_text='Enter company registration number')
    registered_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='reg_address', help_text="Select Registration Address")
    auth_code = models.BigIntegerField(blank=True, help_text='Enter Authentication Code')
    trading_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='trade_address', help_text="Select Trading Address")
    directors_name1 = models.CharField(max_length=100, blank=True, help_text='Enter Directore Name')
    director1_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='director_address', help_text="Select Director 1 Address")
    directors_name2 = models.CharField(max_length=100, blank=True, help_text='Enter Director name 2')
    director2_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='director_address2', help_text="Select Director 2 Address")
    certi_incorp = models.FileField(upload_to='incorp_certificates', blank=True, help_text='Upload a copy of certificate incorpation')


"""Bank details related to company"""


class BankDetails(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    bank_name = models.CharField(max_length=200)
    sort_code = models.BigIntegerField(null=True)
    account_number = models.BigIntegerField(null=True)
    iban = models.CharField(max_length=20)
    swift_code = models.CharField(max_length=20)
    banks_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='bank_address')


"""Markets details related to company select"""


class Markets(models.Model):
    name = models.CharField(max_length=200)
  
  
"""Brands details related to company"""


class Brands(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    brand_name = models.CharField(max_length=200)


"""A particular brand in a market"""


class BrandToMarket(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=True, null=True)
    market = models.ForeignKey(Markets, on_delete=models.CASCADE, blank=True, null=True)
    trade_mark = models.CharField(max_length=200, blank=True)


"""Permission to user for each brand that is active in a market"""


class PermissionToStaff(models.Model):
    brand_to_country = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, null=True)
    to_staff = models.ForeignKey('auth.user', on_delete=models.CASCADE, null=True)
    staff_permission = models.ManyToManyField('auth.permission')
