import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Trip(models.Model):
    trip_number = models.IntegerField(default=0)
    def __str__(self):
        return str(self.trip_number)
    #cost = distance
class EmployeeInformation(models.Model):
    employee_name = models.CharField(max_length=200)
    def __str__(self):
        return self.employee_name

class TripDetail(models.Model):
    trip_number = models.ForeignKey(Trip, on_delete=models.CASCADE)
    start = models.CharField(max_length=200, default="")
    end = models.CharField(max_length=200, default="")
    distance = models.FloatField(default=0)
    pub_date = models.DateTimeField('Trip date', default=timezone.now())
    employee_name = models.CharField(max_length=200, default="")
    def calculateCost(self):
        return self.distance*8   
    cost = models.FloatField(default=0)
    calculateCost.admin_order_field = 'cost'
    def __str__(self):
        return str(self.trip_number)

class Evidence(models.Model):
    evidence_detail = models.CharField(max_length=200)
    extra_cost= models.FloatField(default=0)
    def __str__(self):
        return self.evidence_detail
