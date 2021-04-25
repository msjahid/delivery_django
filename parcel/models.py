from django.db import models

# Create your models here.
MERCHANT_NAME = (
    ('styleZone', 'Style Zone'),
)

PRODUCT_TYPE = (
    ('fragile', 'Fragile'),
    ('liquid', 'Liquid'),
)


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Parcel(models.Model):
    merchantName = models.CharField(max_length=20, choices=MERCHANT_NAME, default='styleZone')
    productType = models.CharField(max_length=23, choices=PRODUCT_TYPE, default='liquid')
    invoiceID = models.CharField(max_length=33)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    quantity = models.ForeignKey(Quantity, on_delete=models.SET_NULL, null=True)
    cod = models.CharField(max_length=33)
    returnCharge = models.CharField(max_length=33)

    def __str__(self):
        return self.merchantName, self.productType, self.invoiceID
