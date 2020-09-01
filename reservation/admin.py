from django.contrib import admin
from .models import *


class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'number_of_people')


admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
