from django.shortcuts import render, reverse, redirect
from accounts.decorators import has_permission
from django.http import HttpResponse
from staff.models import StaffApplication
from student.models import StudentApplication
from .forms import applicationForm
from accounts.models import Role

# Create your views here.

@has_permission(perm_name='staff_application_form')
def index(request):
    if request.method=="POST":
        # post request 
        # create application resource in db
        StaffApplication.objects.create(email=request.user.email, phoneno = request.POST.get('phoneno'), fromDate = request.POST.get('fromDate'), toDate = request.POST.get('toDate'), reason = request.POST.get('reason'), role = request.user.role)

        return redirect(reverse("staff_index"))
    else:
        # fetch pending applications from db
        queryset = StaffApplication.objects.filter(email=request.user.email, status=-1)

        if queryset:
            # render pending applications page
            return render(request, "leaveSystem/application_view.html", {
                "applications" : queryset
            })

        # render applications form page
        return render(request, "leaveSystem/application.html", {
            "form": applicationForm(),
            "action" : "staff_index"
        })

@has_permission('self_staff_applications')
def history(request):
    fields = ['Email', "Phone No", "From Date", "To Date", "Reason", "Status"]
    # fetch requests from db
    queryset = StaffApplication.objects.filter(email=request.user.email).order_by('-created_at')

    # render applications page
    return render(request, "leaveSystem/application_request.html", {
        "fields" : fields,
        "applications" : queryset
    })

@has_permission(perm_name='staff_applications')
def staff_requests(request):
    # fetch pending student requests
    fields = ['Email', "Phone No", "From Date", "To Date", "Reason", "Status", "Action"]
    staff = Role.objects.get(name='staff')
    queryset = staff.staff_applications.filter(status=-1)
    # render applications page
    return render(request, "leaveSystem/application_request.html", {
        "fields" : fields,
        "applications" : queryset
    })

@has_permission(perm_name='staff_applications')
def respond_requests(request, id, is_approved):
    staff = StaffApplication.objects.get(id = id)
    staff.status = is_approved
    staff.save()
    return redirect(reverse("staffRequests"))
