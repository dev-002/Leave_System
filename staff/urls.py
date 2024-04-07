from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="staff_index"),
    path('studentRequests', views.student_requests, name="studentRequests"),
]
