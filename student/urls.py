from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="student_index"),
    path('studentRequests', views.student_requests, name="studentRequests"),
    path('parent_confirmation/<int:id>/<int:action>', views.parent_confirmation, name="parentConfirmation"),
    path('respond/<int:id>/<int:is_approved>', views.respond_requests, name="studentRespondRequests"),
    path('student_history', views.history, name="studentHistory"),
]
