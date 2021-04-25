from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Parcel, Quantity
from .forms import PersonForm


class ParcelListView(ListView):
    model = Parcel
    context_object_name = 'delivery'


class ParcelCreateView(CreateView):
    model = Parcel
    form_class = PersonForm
    success_url = reverse_lazy('parcel_changelist')


class ParcelUpdateView(UpdateView):
    model = Parcel
    form_class = PersonForm
    success_url = reverse_lazy('parcel_changelist')


def load_quantities(request):
    location_id = request.GET.get('location')
    quantities = Quantity.objects.filter(location_id=location_id).order_by('merchantName')
    return render(request, 'hr/quantity_dropdown_list_options.html', {'quantities': quantities})
