import datetime

from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here:
class Employee(models.Model):
    employee_name = models.CharField(max_length=200, default="")
    def __str__(self):
         return self.employee_name

class Project(models.Model):
    project_name = models.CharField(max_length=200, default="")
    def __str__(self):
         return self.project_name

class Trip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,default = None, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,default = None, null = True)

    post_date = models.DateTimeField('post date', auto_now_add=True)


class TripDetail(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE,default = None)

    start = models.CharField(max_length=200, default="")
    end = models.CharField(max_length=200, default="")
    distance = models.FloatField(default=0)
    trip_date = models.DateTimeField('Trip date', default=None)

    def __str__(self):
         return self.start

    @property
    def cost(self):
        return self.distance * 8


class Evidence(models.Model):
    TripDetail = models.ForeignKey(TripDetail, on_delete=models.CASCADE,default = None)
    
    evidence_detail = models.CharField(max_length=200)
    extra_cost= models.FloatField(default=0)

    def __str__(self):
        return self.evidence_detail
        