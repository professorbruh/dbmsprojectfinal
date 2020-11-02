from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(customer_information)
admin.site.register(painting_information)
admin.site.register(sales_information)
