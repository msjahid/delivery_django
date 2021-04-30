
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ParcelListView.as_view(), name='parcel_list'),
    path('add/', views.ParcelCreateView.as_view(template_name='parcel_form.html'), name='parcel_add'),
    path('<int:pk>/', views.ParcelUpdateView.as_view(), name='parcel_edit'),
]