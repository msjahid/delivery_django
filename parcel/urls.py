
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ParcelListView.as_view(), name='parcel_changelist'),
    path('add/', views.ParcelCreateView.as_view(), name='parcel_add'),
    path('<int:pk>/', views.ParcelUpdateView.as_view(), name='parcel_change'),
    path('ajax/load-quantities/', views.load_quantities, name='ajax_load_quantities'),
]