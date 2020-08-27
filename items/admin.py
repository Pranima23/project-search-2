from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no')
    

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'item_type', 'about_item', 'image')


class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'number_of_people')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('reservation_detail', 'complete')


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'decoration_type', 'decoration_cost', 'decoration_description')


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(Event, EventAdmin)