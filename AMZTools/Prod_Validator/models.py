import imp
from operator import mod
from pyexpat import model
from django.db import models
from Business_Admin.models import BrandToMarket

class KeyWord(models.Model):
    brand = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name


"""Cerebro file is saved"""


class ManualValidator(models.Model):
    brand = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True, null=True)
    keyword_auto_validate = models.CharField(max_length=100, blank=True)
    asin1 = models.CharField(blank=True, max_length=30)
    asin2 = models.CharField(blank=True, max_length=30)
    asin3 = models.CharField(blank=True, max_length=30)
    asin4 = models.CharField(blank=True, max_length=30)
    asin5 = models.CharField(blank=True, max_length=30)
    asin6 = models.CharField(blank=True, max_length=30)
    asin7 = models.CharField(blank=True, max_length=30)
    asin8 = models.CharField(blank=True, max_length=30)
    asin9 = models.CharField(blank=True, max_length=30)
    asin10 = models.CharField(blank=True, max_length=30)
    xray_graph = models.FileField(upload_to='manual_validator/x-ray graphs', blank=True)
    xray_ss = models.FileField(upload_to='manual_validator/x-ray ss', blank=True)
    google_trends_ss = models.FileField(upload_to='manual_validator/google trends ss', blank=True)
    xray = models.FileField(upload_to='manual_validator/xray', blank=True)
    cerebro = models.FileField(upload_to='manual_validator/cerebro', blank=True)
    amazon_choice = models.FileField(upload_to='manual_validator/amazon choice', blank=True)
    magnet = models.FileField(upload_to='manual_validator/magnet', blank=True)


"""Column Heading"""


class ManualValidatorHead(models.Model):
    keyword = models.OneToOneField(ManualValidator, on_delete=models.CASCADE, blank=True, null=True)
    phrase = models.CharField(max_length=1000, blank=True)
    search_volume = models.CharField(max_length=1000, blank=True)
    title_density = models.CharField(max_length=1000,null=True, blank=True)
    position = models.CharField(max_length=1000,null=True, blank=True)
    asin2 = models.CharField(max_length=1000, blank=True)
    asin3 = models.CharField(max_length=1000, blank=True)
    asin4 = models.CharField(max_length=1000, blank=True)
    asin5 = models.CharField(max_length=1000, blank=True)
    asin6 = models.CharField(max_length=1000, blank=True)
    asin7 = models.CharField(max_length=1000, blank=True)
    asin8 = models.CharField(max_length=1000, blank=True)
    asin9 = models.CharField(max_length=1000, blank=True)
    asin10 = models.CharField(max_length=1000, blank=True)
    asin11 = models.CharField(max_length=1000, blank=True)


"""Original data"""


class ManualValidatorData(models.Model):
    head = models.ForeignKey(ManualValidatorHead, on_delete=models.CASCADE, blank=True, null=True)
    phrase = models.CharField(max_length=1000, blank=True)
    search_volume = models.CharField(max_length=1000, blank=True)
    title_density = models.CharField(max_length=1000,null=True, blank=True)
    position = models.CharField(max_length=1000,null=True, blank=True)
    asin2 = models.CharField(max_length=1000, blank=True)
    asin3 = models.CharField(max_length=1000, blank=True)
    asin4 = models.CharField(max_length=1000, blank=True)
    asin5 = models.CharField(max_length=1000, blank=True)
    asin6 = models.CharField(max_length=1000, blank=True)
    asin7 = models.CharField(max_length=1000, blank=True)
    asin8 = models.CharField(max_length=1000, blank=True)
    asin9 = models.CharField(max_length=1000, blank=True)
    asin10 = models.CharField(max_length=1000, blank=True)
    asin11 = models.CharField(max_length=1000, blank=True)


class ManualValidatorDataFilter(models.Model):
    mv = models.OneToOneField(ManualValidator, on_delete=models.CASCADE, blank=True, null=True)
    min_sv = models.BigIntegerField(null=True)
    min_relavency = models.BigIntegerField(null=True)
    max_rank = models.BigIntegerField(null=True)


class ManualValidatorDataFilterResult(models.Model):
    filter = models.OneToOneField(ManualValidatorDataFilter, on_delete=models.CASCADE, blank=True, null=True)
    search_volume_total = models.PositiveBigIntegerField(null=True)
    top_10_sv = models.CharField(null=True, blank=True, max_length=5000)
    top_10percent_sv = models.CharField(null=True, blank=True, max_length=5000)
    top_30_sv = models.CharField(null=True, blank=True, max_length=5000)
    top_30percent_sv = models.CharField(null=True, blank=True, max_length=5000)


class ManualValidatorFilteredData(models.Model):
    mv_filtered_result = models.ForeignKey(ManualValidatorDataFilterResult, on_delete=models.CASCADE, blank=True, null=True)
    phrase = models.CharField(max_length=1000, blank=True)
    search_volume = models.CharField(max_length=1000, blank=True)
    asin2 = models.CharField(max_length=1000, blank=True)
    asin3 = models.CharField(max_length=1000, blank=True)
    asin4 = models.CharField(max_length=1000, blank=True)
    asin5 = models.CharField(max_length=1000, blank=True)
    asin6 = models.CharField(max_length=1000, blank=True)
    asin7 = models.CharField(max_length=1000, blank=True)
    asin8 = models.CharField(max_length=1000, blank=True)
    asin9 = models.CharField(max_length=1000, blank=True)
    asin10 = models.CharField(max_length=1000, blank=True)
    asin11 = models.CharField(max_length=1000, blank=True)
