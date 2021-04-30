from django.db import models
from django.utils.translation import gettext_lazy as _


class Merchant(models.Model):
    name = models.CharField(max_length=20, unique=True)
    contact = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        verbose_name_plural = 'Merchants'

    def __str__(self):
        return self.name


# # class Charge(models.Model):
# #     location = models.CharField(max_length=100, unique=True)
# #     quantity = models.CharField(max_length=50)
# #     price = models.PositiveIntegerField()
#
#     class Meta:
#         verbose_name_plural = 'Charges'
#
#     def __str__(self):
#         return self.location


class Order(models.Model):
    class ProductType(models.TextChoices):
        FRAGILE = 'frg', _('Fragile')
        LIQUID = 'lqd', _('Liquid')

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant_order')
    product_type = models.CharField(max_length=10, choices=ProductType.choices, default=ProductType.FRAGILE)
    invoice_id = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=100, unique=True)
    quantity = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    order_datetime = models.DateField(auto_now_add=True, editable=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.invoice_id


