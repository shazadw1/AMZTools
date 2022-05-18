from django.contrib import admin
from . models import *
# Register your models here.


class ManualValidatorAdmin(admin.ModelAdmin):
    list_display = ['brand' ,'keyword_auto_validate','asin1','asin2',
    'asin3',
    'asin4',
    'asin5',
    'asin6',
    'asin7',
    'asin8',
    'asin9',
    'asin10',
    'xray_graph',
    'xray_ss',
    'google_trends_ss',
    'cerebro']


class ManualValidatorHeadAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'phrase','search_volume','title_density','position','asin2',
    'asin3',
    'asin4',
    'asin5',
    'asin6',
    'asin7',
    'asin8',
    'asin9',
    'asin10',
    'asin11']


class ManualValidatorDataAdmin(admin.ModelAdmin):
    list_display = ['head', 'phrase','search_volume','title_density','position','asin2',
    'asin3',
    'asin4',
    'asin5',
    'asin6',
    'asin7',
    'asin8',
    'asin9',
    'asin10',
    'asin11']



admin.site.register(KeyWord)
admin.site.register(ManualValidator, ManualValidatorAdmin)
admin.site.register(ManualValidatorHead, ManualValidatorHeadAdmin)
admin.site.register(ManualValidatorData, ManualValidatorDataAdmin)
