import imp
from operator import mod
from django.db import models
from Business_Admin.models import BrandToMarket

class KeyWord(models.Model):
    brand = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name


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


class ManualValidatorHead(models.Model):
    keyword = models.ForeignKey(ManualValidator, on_delete=models.CASCADE, blank=True, null=True, unique=True)
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

class ManualValidatorData(models.Model):
    head = models.ForeignKey(ManualValidatorHead, on_delete=models.CASCADE, blank=True, null=True, unique=True)
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

