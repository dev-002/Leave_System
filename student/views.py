from django.shortcuts import render, reverse, redirect
from accounts.decorators import has_permission
from django.http import HttpResponse
from student.models import StudentApplication
from .forms import applicationForm
from accounts.models import Role

# Create your views here.

@has_permission(perm_name='student_application_form')
def index(request):
    if request.method=="POST":
        # post request 
        # create application resource in db
        StudentApplication.objects.create(email=request.user.email, parentEmail = request.POST.get('parentEmail'), rollno = request.POST.get('rollno'), phoneno = request.POST.get('phoneno'), fatherName = request.POST.get('fatherName'), branch = request.POST.get('branch'), semester = request.POST.get('semester'), hostelNumber = request.POST.get('hostelNumber'), roomNumber = request.POST.get('roomNumber'), fromDate = request.POST.get('fromDate'), toDate = request.POST.get('toDate'), reason = request.POST.get('reason'), parentContact = request.POST.get('parentContact'), role = request.user.role)

        return redirect(reverse("student_index"))
    else:
        # fetch pending applications from db
        queryset = StudentApplication.objects.filter(email=request.user.email, status=-1)

        if queryset:
            # render pending applications page
            return render(request, "leaveSystem/application_view.html", {
                "applications" : queryset,
            })

        # render applications form page
        return render(request, "leaveSystem/application.html", {
            "form": applicationForm(),
            "action" : "student_index"
        })

@has_permission('self_student_applications')
def history(request):
    fields = ['Email', "Parent's Email", "Roll No", "Phone No", "Father's Name", "Branch", "Semester", "Hostel Number", "Room Number",
    "From Date", "To Date", "Reason", "Parent's Contact", "Status", "Parent Responded"]
    # fetch requests from db
    queryset = StudentApplication.objects.filter(email=request.user.email).order_by('-created_at')

    # render applications page
    return render(request, "leaveSystem/application_request.html", {
        "fields" : fields,
        "applications" : queryset
    })

@has_permission(perm_name='student_applications')
def student_requests(request):
    # fetch pending student requests
    fields = ['Email', "Parent's Email", "Roll No", "Phone No", "Father's Name", "Branch", "Semester", "Hostel Number", "Room Number",
    "From Date", "To Date", "Reason", "Parent's Contact", "Status", "Parent Responded", "Action"]
    student = Role.objects.get(name='student')
    queryset = student.student_applications.filter(status=-1)
    # render applications page
    return render(request, "leaveSystem/application_request.html", {
        "fields" : fields,
        "applications" : queryset
    })

def parent_confirmation(request, id, action):
    # update db
    queryset = StudentApplication.objects.filter(id=id)
    if not queryset:
        return HttpResponse("No Response recorded")
    queryset[0].parent_responded = action
    queryset[0].save()
    
    return HttpResponse("Your Response is recorded")

@has_permission(perm_name='student_applications')
def respond_requests(request, id, is_approved):
    student = StudentApplication.objects.get(id = id)
    student.status = is_approved
    student.save()
    return redirect(reverse("studentRequests"))