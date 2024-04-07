from django.db import models
from django.contrib.auth.models import AbstractUser

# Permission: 
# 'self_staff_applications', 
# 'self_student_applications',
# 'staff_applications',
# 'student_applications',
# 'student_application_form',
# 'staff_application_form'

class Permission(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)

    # ROLES
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"