from django.db import models
from accounts.models import Role

class StaffApplication(models.Model):
    email=models.EmailField(max_length=50)
    phoneno=models.IntegerField(blank=True, null=True)
    hostelNumber=models.CharField(max_length=255, blank=True, null=True)
    roomNumber=models.IntegerField(blank=True, null=True)
    fromDate=models.DateField(blank=True, null=True)
    time=models.TimeField(blank=True, null=True)
    toDate=models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)

    # status choices
    PENDING = -1
    REJECTED = 0
    APPROVED = 1
    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (REJECTED, 'Rejected'),
        (APPROVED, 'Approved'),
    )
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    
    # role
    role=models.ForeignKey(Role, related_name="staff_applications", on_delete=models.CASCADE, null=True)