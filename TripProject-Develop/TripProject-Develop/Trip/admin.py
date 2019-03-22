from django.contrib import admin

from .models import Trip
from .models import TripDetail
from .models import Evidence
from django.utils import timezone


class EvidencelInline(admin.StackedInline):
    model = Evidence
    extra = 1
    
class TripDetailInline(admin.StackedInline):
    model = TripDetail
    extra = 2
    inlines = [EvidencelInline]

    
class TripAdmin(admin.ModelAdmin):
    list_display = ('employee_name','post_date')
#    fieldsets = [
#        (None,               {'fields': ['trip_number','employee_name','post_date']}),
#        ('Trip7888',             {'fields': ['trip_number','post_date']}),
#     ]
    inlines = [TripDetailInline]

admin.site.register(Trip,TripAdmin)