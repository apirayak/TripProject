import datetime

from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.




class Trip(models.Model):
    employee_name = models.CharField(max_length=200, default="")
    post_date = models.DateTimeField('post date', auto_now_add=True)
    project_name = models.CharField(max_length=200, default="")
# class EmployeeInformation(models.Model):
#     employee_name = models.CharField(max_length=200)
    def __str__(self):
         return self.employee_name

class TripDetail(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE,default = None)

    start = models.CharField(max_length=200, default="")
    end = models.CharField(max_length=200, default="")
    distance = models.FloatField(default=0)
    trip_date = models.DateTimeField('Trip date', default=None)

    @property
    def cost(self):
        return self.distance * 8
    
   # def __str__(self):
    #     return self.id

class Evidence(models.Model):
    TripDetail = models.ForeignKey(TripDetail, on_delete=models.CASCADE,default = None)

    evidence_detail = models.CharField(max_length=200)
    extra_cost= models.FloatField(default=0)
    def __str__(self):
        return self.evidence_detail