from unicodedata import name
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from leaveSystem.models import applicationModel, account_data
import random
from django.core.mail import send_mail, EmailMultiAlternatives
from .forms import applicationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from . import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags



applications = {}

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return HttpResponseRedirect(reverse("application"))

@login_required(login_url="login")
def deleteSessionOrAccountData(request, key):
    if request.user.is_authenticated:
        username = request.user.username
        account_data.objects.filter(username=username).delete()
    else:
        del request.session[key]

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if bool(account_data.objects.filter(username=username)):
                obj = account_data.objects.get(username=request.user.username)
                if obj and int(obj.value) in applications:
                    request.session["id"]=int(obj.value)
                else:
                    deleteSessionOrAccountData(request,key="id")
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "leaveSystem/login.html", {
                "message":"Invalid Credentials"
            })
    else:
        return render(request, "leaveSystem/login.html")

def logout_view(request):
    if not account_data.objects.filter(username=request.user.username) and "id" in request.session and request.session["id"] in applications:
        record = account_data(username=request.user.username, 
                                    key="id", 
                                    value=str(request.session["id"]))
        record.save()
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required(login_url="login")
def application(request):
    if "id" in request.session and request.session["id"] in applications:
        return HttpResponseRedirect(reverse("applicationView"))
    elif request.method=="POST":
        id = random.randint(0, 1000)
        while id in applications:
            id = random.randint(0, 1000)
        print(request.POST.dict())
        applications[id] = request.POST.dict()
        applications[id]['status'] = -1
        applications[id]['parent_responded'] = False
        request.session["id"] = id
        request.session.modified = True

        # here to be changed
        template = render_to_string('leaveSystem/parent_confirmation.html', {
            'id': id,
            'application': applications[id]
        })
        text_content = strip_tags(template)
        email = EmailMultiAlternatives(
            'Leave Application Confirmation',
            text_content,
            settings.EMAIL_HOST_USER,
            [applications[id]['parentEmail']]
        )
        email.attach_alternative(template, "text/html")
        email.send()
        return HttpResponseRedirect(reverse("applicationView"))
    else:
        return render(request, "leaveSystem/application.html", {
            "form": applicationForm()
        })

@login_required(login_url="login")
def application_view(request):
    if "id" in request.session and request.session["id"] in applications:
        return render(request, "leaveSystem/application_view.html", {
            "application": applications[request.session["id"]]
        })
    else:
        return render(request, "leaveSystem/application_view.html")

@login_required
@user_passes_test(lambda u: u.is_superuser)
def application_requests(request):
    if len(applications) > 0:
        return render(request, "leaveSystem/application_requests.html", {
            'application': applications
        })
    else:
        return render(request, "leaveSystem/application_requests.html")

@login_required
@user_passes_test(lambda u: u.is_superuser)
def respond_requests(request, id, is_approved):
    if id in applications:
        # print(applications[id])
        applications[id]['status'] = is_approved
        email=applications[id]['email']
        name=applications[id]['name']
        rollno=applications[id]['rollno']
        phoneno=applications[id]['phoneno']
        fatherName=applications[id]['fatherName']
        branch=applications[id]['branch']
        semester=applications[id]['semester']
        hostelNumber=applications[id]['hostelNumber']
        roomNumber=applications[id]['roomNumber']
        fromDate=applications[id]['fromDate']
        time=applications[id]['time']
        toDate=applications[id]['toDate']
        reason=applications[id]['reason']
        parentContact=applications[id]['parentContact']
        status="Approved" if applications[id]['status'] == 1 else "Rejected"

        # We can save approved or rejected requests here
        f = applicationModel(name=name, rollno=rollno, phoneno=phoneno, fatherName=fatherName, branch=branch, semester=semester, hostelNumber=hostelNumber, roomNumber=roomNumber, fromDate=fromDate, time=time, toDate=toDate, reason=reason, parentContact=parentContact, status=status)
        f.save()
        # Mail service can also be provided here
        message = f'Your leave application from {fromDate} to {toDate} has been {status}'
        send_mail(
            'Leave Application',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        applications.pop(id)
        return HttpResponse("True")
    else:
        return HttpResponse("Error")
    
def parent_confirmation(request):
    id = int(request.GET.get('id'))
    action = bool(request.GET.get('action'))
    if id in applications:
        print("parent response recorded")
        applications[id]['parent_responded'] = True
        applications[id]['parent_response'] = action
    return HttpResponse("Your Response is recorded")
