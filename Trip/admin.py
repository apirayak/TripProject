from django.contrib import admin

import nested_admin

from .models import Trip
from .models import TripDetail
from .models import Evidence
from .models import Employee
from .models import Project
from django.utils import timezone


class EmployeeAdmin(nested_admin.NestedModelAdmin):
    fields = ('employee_name' ,)

class ProjectAdmin(nested_admin.NestedModelAdmin):
    fields = ('project_name' ,)

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
    list_display = ('get_employee_name', 'get_project_name','calculate_cost', 'post_date')
    readonly_fields = ('calculate_cost','calculate_extra',)

    # fieldsets = (
    #   ('Standard info', {
    #       'fields': ('name')
    #   }),
    #   ('Address info', {
    #       'fields': ('address', ('city', 'zip'))
    #   }),
    # )
    def calculate_cost(self, obj):
        details = obj.tripdetail_set.all()
        base = 0
        for detail in details:
            base = base + detail.cost
        return base
        
    def calculate_extra(self,obj):
        extras = obj.tripdetail_set.all().Evidence_set.all()
        total_extra = 0
        for extra in extras:
            total_extra = total_extra + extra.extra_cost
        return total_extra

    def total(self,obj):
        pass

    def get_employee_name(self, obj):
        return obj.employee.employee_name
    get_employee_name.short_description = 'Employee name'
    get_employee_name.admin_order_field = 'employee__employee_name'

    def get_project_name(self, obj):
        return obj.project.project_name
    get_project_name.short_description = 'Project name'
    get_project_name.admin_order_field = 'project__project_name'

    calculate_cost.short_description = 'calculate cost'
    inlines = (TripDetailInline,)

admin.site.register(Trip,TripAdmin)

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Project,ProjectAdmin)