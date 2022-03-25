from django.db import models
from Business_Admin.models import BrandToMarket

class DesignVideo(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)

