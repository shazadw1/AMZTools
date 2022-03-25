from django.db import models
from Business_Admin.models import BrandToMarket


class Comp_Analysis_basic_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)


class Comp_Analysis_kw_cerebro_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)


class Comp_Analysis_kw_amz_choice_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)


class Comp_Analysis_kw_magnet_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)


class Comp_Analysis_kw_ba_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)


class Comp_Analysis_kw_ba_output_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)


class Comp_Analysis_kw_master_kw_data(models.Model):
    brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE)
    key_word = models.CharField(max_length=100, blank=True)
