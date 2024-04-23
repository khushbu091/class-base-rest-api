from django.db import models

# Create your models here.
class Employee(models.Model):
    empName=models.CharField(max_length=50)
    empJdate=models.DateField()
    empAddress=models.CharField(max_length=50)
    empContact=models.IntegerField()


