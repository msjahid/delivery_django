from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Order
from .forms import ParcelForm


class ParcelListView(ListView):
    model = Order
    context_object_name = 'parcels'
    template_name = 'parcel_list.html'


class ParcelCreateView(CreateView):
    model = Order
    form_class = ParcelForm
    success_url = reverse_lazy('parcel_list')


class ParcelUpdateView(UpdateView):
    model = Order
    form_class = ParcelForm
    success_url = reverse_lazy('parcel_list')
