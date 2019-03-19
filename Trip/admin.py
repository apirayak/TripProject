from django.contrib import admin

from .models import Trip
from .models import TripDetail

admin.site.register(TripDetail)
admin.site.register(Trip)