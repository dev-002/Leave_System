from django.contrib import admin
from .models import applicationModel, account_data

admin.site.register(applicationModel)
admin.site.register(account_data)