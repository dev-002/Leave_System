from django.shortcuts import render, reverse, redirect
from accounts.decorators import has_permission
from django.http import HttpResponse
from staff.models import StaffApplication
from accounts.models import Role
from .forms import applicationForm

# Create your views here.

@has_permission(perm_name='staff_application_form')
def index(request):
    if request.method=="POST":
        # post request 
        # create application resource in db
        StaffApplication.objects.create(email=request.user.email, phoneno = request.POST.get('phoneno'), fromDate = request.POST.get('fromDate'), time = request.POST.get('time'), toDate = request.POST.get('toDate'), reason = request.POST.get('reason'), role = request.user.role)

        return redirect(reverse("staffApplicationView"))
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

@has_permission(perm_name='student_applications')
def student_requests(request):
    # fetch pending student requests
    student = Role.objects.get(name='student')
    queryset = student.student_applications.filter(status=-1)
    # render applications page
    return render(request, "leaveSystem/application_view.html", {
        "applications" : queryset
    })