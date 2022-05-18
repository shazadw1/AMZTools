from django.db import models
from Business_Admin.models import BrandToMarket


class ppc_gen_basic_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)


class ppc_gen_groups_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)


class ppc_gen_kw_group_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)


class ppc_gen_output_bulk_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    key_word = models.CharField(max_length=100, blank=True)
