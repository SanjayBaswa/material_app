from django.db import models
import datetime

# Create your models here.


class Datatable(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    dc_no = models.IntegerField()
    Part_no = models.CharField(max_length=200)
    returnable = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    date = models.DateField()
    time_stamp =models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.project 
  
      
