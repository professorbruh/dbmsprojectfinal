from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(tiers)
@admin.register(painting_information)
@admin.register(tiers_customer)
@admin.register(warehouse)
@admin.register(warehouse_painting)
@admin.register(order_information)
class Paint_Info(admin.ModelAdmin):
    search_fields = ("painting_id__startswith",)
class Order_Info(admin.ModelAdmin):
    search_fields = ("user__startswith","painting__startwith",)

