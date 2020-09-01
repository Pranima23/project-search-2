from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_no', 'password')


admin.site.register(Customer, CustomerAdmin)
