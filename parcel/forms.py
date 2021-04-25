from django import forms
from .models import Parcel, Quantity


class PersonForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ('merchantName', 'productType', 'id', 'location', 'quantity', 'cod', 'returnCharge')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].queryset = Quantity.objects.none()

        if 'location' in self.data:
            try:
                location_id = int(self.data.get('location'))
                self.fields['quantity'].queryset = Quantity.objects.filter(location_id=location_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['quantity'].queryset = self.instance.location.quantity_set.order_by('name')
