from django.shortcuts import render, reverse, redirect
from accounts.decorators import has_permission
from django.http import HttpResponse
from student.models import StudentApplication
from .forms import applicationForm

# Create your views here.

@has_permission(perm_name='student_application_form')
def index(request):
    if request.method=="POST":
        # post request 
        # create application resource in db
        StudentApplication.objects.create(email=request.user.email, parentEmail = request.POST.get('parentEmail'), rollno = request.POST.get('rollno'), phoneno = request.POST.get('phoneno'), fatherName = request.POST.get('fatherName'), branch = request.POST.get('branch'), semester = request.POST.get('semester'), hostelNumber = request.POST.get('hostelNumber'), roomNumber = request.POST.get('roomNumber'), fromDate = request.POST.get('fromDate'), time = request.POST.get('time'), toDate = request.POST.get('toDate'), reason = request.POST.get('reason'), parentContact = request.POST.get('parentContact'), role = request.user.role)

        return redirect(reverse("student_index"))
    else:
        # fetch pending applications from db
        queryset = StudentApplication.objects.filter(email=request.user.email, status=-1)

        if queryset:
            # render pending applications page
            return render(request, "leaveSystem/application_view.html", {
                "applications" : queryset
            })

        # render applications form page
        return render(request, "leaveSystem/application.html", {
            "form": applicationForm(),
            "action" : "student_index"
        })

def parent_confirmation(request, id, action):
    # update db
    queryset = StudentApplication.objects.filter(id=id)
    if not queryset:
        return HttpResponse("No Response recorded")
    queryset[0].parent_responded = action
    queryset[0].save()
    
    return HttpResponse("Your Response is recorded")