from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="student_index"),
    path('parent_confirmation/<int:id>/<int:action>', views.parent_confirmation, name="parentConfirmation"),
]
