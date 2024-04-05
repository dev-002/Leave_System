from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Role)
admin.site.register(Permission)

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Your custom logic goes here
        # For example, if you want to modify some fields before saving:
        obj.set_password(obj.password)
        obj.save()

admin.site.register(CustomUser, CustomUserAdmin)