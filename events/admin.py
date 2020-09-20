from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'decoration_type', 'decoration_cost', 'decoration_description')


class BookEventAdmin(admin.ModelAdmin):
    list_display = ('customer', 'event')


admin.site.register(Event, EventAdmin)
admin.site.register(BookEvent, BookEventAdmin)