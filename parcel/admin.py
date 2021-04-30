from django.contrib import admin
from .models import Merchant, Order

admin.site.site_header = "Delivery System"


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact', 'address']
    list_display_links = ['name']
    list_filter = ['name']


# @admin.register(Charge)
# class ChargeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'location', 'quantity', 'charge']
#     list_display_links = ['location']
#     list_filter = ['location', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchant', 'product_type', 'invoice_id', 'location', 'quantity', 'price', 'order_datetime']
    list_display_links = ['merchant']
    list_filter = ['merchant']
