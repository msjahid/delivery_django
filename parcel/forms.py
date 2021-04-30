from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['merchant', 'product_type', 'invoice_id', 'location', 'quantity', 'price']

