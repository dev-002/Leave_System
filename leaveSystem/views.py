from unicodedata import name
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
import random
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required, user_passes_test
from . import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def index(request):
    # redirect to respective roles based on their roles
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.user.role.name == "admin":
        return redirect(reverse('staffRequests'))
    elif request.user.role.name == "staff":
        return redirect(reverse('staff_index'))
    else:
        return redirect(reverse('student_index'))

# for login purpose
def login_view(request):
    if request.method == "POST":
        # fetch post data
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check if user exists
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Invalid email")
            return redirect(reverse("login"))

        # authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # user is authenticated creating session using login
            login(request, user)
            # redirect to index
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, "leaveSystem/login.html")
    else:
        return render(request, "leaveSystem/login.html")

# for logout purpose
@login_required(login_url="login")
def logout_view(request):
    # logout and delete session
    logout(request)
    return HttpResponseRedirect(reverse("login"))