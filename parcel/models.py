from django.db import models

# Create your models here.


class Merchant(models.Model):
    merchantName = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'merchant'

    def __str__(self):
        return self.merchantName


class Product(models.Model):
    productType = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.productType


class Charge(models.Model):
    location = models.CharField(max_length=20)
    quantity = models.CharField(max_length=10)
    charge = models.CharField(max_length=20)
    cod = models.CharField(max_length=10)
    returnCharge = models.CharField(max_length=15)

    class Meta:
        db_table = 'charge'

    def __str__(self):
        return self.location


class Order(models.Model):
    merchant_name = models.ForeignKey('Merchant', on_delete=models.CASCADE)
    product_type = models.ForeignKey('Product', on_delete=models.CASCADE)
    invoiceID = models.CharField(max_length=33)
    product_charge = models.ForeignKey('Charge', on_delete=models.CASCADE)
    total = models.CharField(max_length=15)
    order_data = models.DateField(auto_now_add=True, editable=True, blank=True, null=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.invoiceID

# class Parcel(models.Model):
#     merchantName = models.CharField(max_length=20, choices=MERCHANT_NAME, default='Style Zone')
#     productType = models.CharField(max_length=20, choices=PRODUCT_TYPE, default='Fragile')
#     invoiceID = models.CharField(max_length=33)
#     location = models.CharField(max_length=20, choices=LOCATION, default='Inside of Dhaka')
#     quantity = models.CharField(max_length=20, choices=QUANTITY, default='500 gm to 2 kg')
#     charge = models.CharField(max_length=20)
#     cod = models.CharField(max_length=10)
#     returnCharge = models.CharField(max_length=15)
#     total = models.CharField(max_length=15)
