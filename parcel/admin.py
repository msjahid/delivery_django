from django.contrib import admin
from .models import Order
from .models import Merchant
from .models import Charge
from .models import Product


# Register your models here.

# Type
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchantName', 'productType', 'invoiceID', 'location', 'quantity', 'charge', 'cod',
                    'returnCharge', 'total', 'order_data']
    list_display_links = ['id']
    list_filter = ['invoiceID']
    ordering = ['-id']


admin.site.register(Merchant)
admin.site.register(Charge)
admin.site.register(Product)
