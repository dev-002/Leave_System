from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="staff_index"),
    path('staff_history', views.history, name="staffHistory"),
    path('staffRequests', views.staff_requests, name="staffRequests"),
    path('respond/<int:id>/<int:is_approved>', views.respond_requests, name="staffRespondRequests"),
]
