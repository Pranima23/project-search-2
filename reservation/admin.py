from django.contrib import admin
from .models import *


class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'number_of_people', 'check_in', 'check_out')


admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
