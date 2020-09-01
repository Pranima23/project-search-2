from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'decoration_type', 'decoration_cost', 'decoration_description')


admin.site.register(Event, EventAdmin)