from django.db import models
from Business_Admin.models import BrandToMarket

class listing_basic_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)


class listing_output_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)
