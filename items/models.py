from django.db import models
from registration.models import Customer
from reservation.models import *


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    about_item = models.TextField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='item_image', blank=True)
    item_type_choices = (
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Drinks', 'Drinks'),
    )
    item_type = models.CharField(max_length = 20, choices = item_type_choices, default = '')


class Order(models.Model):
    reservation_detail = models.OneToOneField(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)

    @property
    def get_order_total(self):
        orderdetails = self.orderdetails_set.all()
        total = sum([item.get_item_total for item in orderdetails])


class OrderDetails(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()

    @property
    def get_item_total(self):
        total = self.item.price * self.quantity



