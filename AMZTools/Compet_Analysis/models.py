from click import File
from django.db import models
from Business_Admin.models import BrandToMarket


# compt analysis basic data


class Comp_Analysis_basic_data(models.Model):
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
    xray_graph = models.FileField(upload_to='compt_analysis/x-ray graphs', blank=True)
    xray_ss = models.FileField(upload_to='compt_analysis/x-ray ss', blank=True)
    google_trends_ss = models.FileField(upload_to='compt_analysis/google trends ss', blank=True)
    xray = models.FileField(upload_to='compt_analysis/xray', blank=True)
    cerebro = models.FileField(upload_to='compt_analysis/cerebro', blank=True)
    amazon_choice = models.FileField(upload_to='compt_analysis/amazon choice', blank=True)
    magnet = models.FileField(upload_to='compt_analysis/magnet', blank=True)
    master_table = models.BooleanField(default=False)


# cerebro head


class Comp_Analysis_KW_Cerebro_Data_Head(models.Model):
    keyword = models.OneToOneField(Comp_Analysis_basic_data, on_delete=models.CASCADE, blank=True, null=True)
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
    excel_file = models.FileField(upload_to='compt_analysis/final_cerebro_excel/', blank=True)


# cerebro data


class Comp_Analysis_KW_Cerebro_Data(models.Model):
    head = models.ForeignKey(Comp_Analysis_KW_Cerebro_Data_Head, on_delete=models.CASCADE, blank=True, null=True)
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


class Comp_Analysis_Data_Filter(models.Model):
    mv = models.OneToOneField(Comp_Analysis_basic_data, on_delete=models.CASCADE, blank=True, null=True)
    min_sv = models.BigIntegerField(null=True)
    min_relavency = models.BigIntegerField(null=True)
    max_rank = models.BigIntegerField(null=True)


class Comp_Analysis_Data_FilterResult(models.Model):
    filter = models.OneToOneField(Comp_Analysis_Data_Filter, on_delete=models.CASCADE, blank=True, null=True)
    total_phrase =  models.PositiveBigIntegerField(null=True)
    search_volume_total = models.PositiveBigIntegerField(null=True)
    top_10_sv = models.CharField(null=True, blank=True, max_length=5000)
    top_10percent_sv = models.CharField(null=True, blank=True, max_length=5000)
    top_30_sv = models.CharField(null=True, blank=True, max_length=5000)
    top_30percent_sv = models.CharField(null=True, blank=True, max_length=5000)
    top_3 = models.CharField(blank=True, max_length=5000)
    filtered_file = models.FileField(upload_to='compt_analysis/filtered_cerebro_excel/', blank=True)


class Comp_Analysis_Filtered_Data(models.Model):
    mv_filtered_result = models.ForeignKey(Comp_Analysis_Data_FilterResult, on_delete=models.CASCADE, blank=True, null=True)
    phrase = models.CharField(max_length=1000, blank=True)
    score = models.IntegerField(null=True, blank=True)
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


# # keyword amazon analysis


# class Comp_Analysis_kw_amz_choice_data(models.Model):
#     brand_to_market = models.OneToOneField(Comp_Analysis_basic_data, on_delete=models.CASCADE, blank=True, null=True)
#     file = models.CharField(max_length=100, blank=True)


# # keyword magnet analysis


# class Comp_Analysis_kw_magnet_data(models.Model):
#     brand_to_market = models.OneToOneField(Comp_Analysis_basic_data, on_delete=models.CASCADE, blank=True, null=True)
#     file = models.CharField(max_length=100, blank=True)


# class Comp_Analysis_kw_ba_data(models.Model):
#     brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True, null=True)
#     key_word = models.CharField(max_length=100, blank=True)


# class Comp_Analysis_kw_ba_output_data(models.Model):
#     brand_to_market = models.ForeignKey(BrandToMarket, on_delete=models.CASCADE, blank=True, null=True)
#     key_word = models.CharField(max_length=100, blank=True)


class Comp_Analysis_kw_master_table(models.Model):
    filtered_comp = models.ForeignKey(Comp_Analysis_basic_data, on_delete=models.CASCADE, blank=True, null=True)
    phrase = models.CharField(max_length=1000, blank=True)
    search_volume = models.CharField(max_length=1000, blank=True)
    title_density = models.CharField(max_length=1000, blank=True)
    source = models.CharField(max_length=1000, blank=True)
    relevancy = models.CharField(max_length=1000, blank=True)
    
