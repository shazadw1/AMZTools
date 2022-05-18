import imp
from django.contrib import admin
from . models import *
from django.contrib.auth.models import Permission
# Register your models here.


# class AddressAdmin(admin.StackedInline):
#     models = Address

# class CompanyAdmin(admin.ModelAdmin):
#     inline = [AddressAdmin]


admin.site.register(Company)
admin.site.register(Address)
admin.site.register(BankDetails)
admin.site.register(Brands)
admin.site.register(Markets)
admin.site.register(BrandToMarket)
admin.site.register(PermissionToStaff)
admin.site.register(Permission)
