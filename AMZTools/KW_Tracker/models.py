from django.db import models
from Business_Admin.models import BrandToMarket

class keyword_tracker(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)


class keyword_rank(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)


class keyword_change(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)
