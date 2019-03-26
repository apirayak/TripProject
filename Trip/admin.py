from django.contrib import admin

import nested_admin

from .models import Trip
from .models import TripDetail
from .models import Evidence
from django.utils import timezone


class EvidencelInline(nested_admin.NestedStackedInline):
    fields = ('evidence_detail','extra_cost',)
    model = Evidence
    extra = 0
    
class TripDetailInline(nested_admin.NestedStackedInline):
    fields = ('trip_date','start', 'end', 'distance', 'cost' ,)
    readonly_fields = ('cost', )
    inlines = (EvidencelInline, )
    model = TripDetail
    extra = 0
    
class TripAdmin(nested_admin.NestedModelAdmin):
    list_display = ('employee_name', 'project_name','calculate_cost', 'post_date')
    readonly_fields = ('calculate_cost',)
    def calculate_cost(self, obj):
        details = obj.tripdetail_set.all()
        base = 0
        for detail in details:
            base = base + detail.cost
        return base
    calculate_cost.short_description = 'calculate cost'
    inlines = (TripDetailInline,)

admin.site.register(Trip,TripAdmin)