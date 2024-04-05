from django.db import models
from accounts.models import Role

class Application(models.Model):
    username=models.CharField(max_length=255)
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

    # status choices
    PENDING = -1
    REJECTED = 0
    APPROVED = 1
    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (REJECTED, 'Rejected'),
        (APPROVED, 'Approved'),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True, default=PENDING)

    # parent response
    parent_responded =  models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True, default=PENDING)
    
    # role
    role=models.ForeignKey(Role, related_name="applications", on_delete=models.CASCADE, null=True)

class account_data(models.Model):
    username = models.CharField(max_length=30)
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30, null=True, blank=True)
