from django.db import models

class applicationModel(models.Model):
    name=models.CharField(max_length=255)
    rollno=models.IntegerField()
    phoneno=models.IntegerField()
    fatherName=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    semester=models.CharField(max_length=255)
    hostelNumber=models.CharField(max_length=255)
    roomNumber=models.IntegerField()
    fromDate=models.DateField()
    time=models.TimeField()
    toDate=models.DateField()
    reason = models.CharField(max_length=500)
    parentContact=models.IntegerField()
    status=models.CharField(max_length=255)

class account_data(models.Model):
    username = models.CharField(max_length=30)
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30, null=True, blank=True)
