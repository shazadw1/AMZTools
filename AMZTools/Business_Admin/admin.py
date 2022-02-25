from inspect import stack
from django.contrib import admin
from . models import *
# Register your models here.


# class AddressAdmin(admin.StackedInline):
#     models = AddressModel

# class CompanyAdmin(admin.ModelAdmin):
#     inline = [AddressAdmin]


admin.site.register(CompanyModel)
admin.site.register(AddressModel)
admin.site.register(BankDetails)
admin.site.register(Brands)
admin.site.register(Markets)
admin.site.register(TradeMark)
