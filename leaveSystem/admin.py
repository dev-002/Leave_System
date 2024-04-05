from django.contrib import admin
from .models import Application, account_data

admin.site.register(Application)
admin.site.register(account_data)