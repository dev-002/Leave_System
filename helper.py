from leaveSystem.models import Application
from accounts.models import *
from accounts.decorators import has_permission

# functions to query db 
@has_permission(perm_name='self_applications')
def pending_requests(username=None):
    queryset = Application.objects.filter(username=username, status=-1)
    return queryset

@has_permission(perm_name='student_applications')
def student_requests(username=None):
    student = Role.objects.get(name='student')
    queryset = student.applications.filter(status=-1)
    return queryset

@has_permission(perm_name='staff_applications')
def staff_requests(username=None):
    staff = Role.objects.get(name='staff')
    queryset = staff.applications.filter(status=-1)
    return queryset
