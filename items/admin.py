from django.contrib import admin
from .models import *
  

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'item_type', 'about_item', 'image')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer',)


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
