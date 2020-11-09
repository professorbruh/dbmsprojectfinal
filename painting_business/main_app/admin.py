from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(customer_information)
class Cust_Admin(admin.ModelAdmin):
    search_fields = ("customer_id__startswith",)

@admin.register(painting_information)
class Paint_Admin(admin.ModelAdmin):
    admin.site.register(sales_information)

class SalesInfo(admin.ModelAdmin):
    search_fields = ("customer_id__starswith",)
