from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Order
from .models import Merchant
from .models import Charge
from .models import Product


class ChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = ['location', 'quantity', 'charge', 'cod', 'returnCharge']


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('merchantName', 'productType', 'invoiceID', 'location', 'quantity', 'charge', 'cod', 'returnCharge',
                  'total')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['merchantName'].label = "Merchant Name"
        self.fields['productType'].label = "Product Type"
        self.fields['invoiceID'].label = "Invoice"
        self.fields['location'].label = "Location"
        self.fields['quantity'].label = "Quantity"
        self.fields['charge'].label = "Charge"
        self.fields['cod'].lable = "Cod"
        self.fields['returnCharge'].label = "Return Charge"
        self.fields['total'].lable = "Total"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save parcel'))
