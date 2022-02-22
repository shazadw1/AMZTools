from django.db import models
from numpy import product

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=100, help_text='Enter Name')
    pricing_per_month = models.IntegerField(help_text='Enter Price for per month')
    description = models.CharField(max_length=100, help_text='Enter Description')
    company_limit = models.IntegerField(help_text='Enter Company Limit')
    users_limit = models.IntegerField(help_text='Enter Users Limit')
    brands_limit = models.IntegerField(help_text='Enter Brand Limit')
    markets_limit = models.IntegerField(help_text='Enter Markets Limit')
    product_validation_limit = models.IntegerField(help_text='Enter Product Validation Limit')
    comp_analysis_limit = models.IntegerField(help_text='Enter Company Analysis limit')
    listings_limit = models.IntegerField(help_text='Enter Listing Limit')
    ppc_generation_limit = models.IntegerField(help_text='Enter PPC Generation Limit')
    ppc_optimization_limit = models.IntegerField(help_text='Enter PPC Optimization Limit')

