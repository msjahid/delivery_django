from django.contrib import admin
from .models import Parcel
from .models import Location
from .models import Quantity

# Register your models here.
admin.site.register(Parcel)
admin.site.register(Location)
admin.site.register(Quantity)
