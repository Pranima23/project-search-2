from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    about_item = models.TextField()
    image = models.ImageField(upload_to='item_image', blank=True)
    item_type_choices = (
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Drinks', 'Drinks'),
    )
    item_type = models.CharField(max_length = 20, choices = item_type_choices, default = '')


class Event(models.Model):
    name_choices=(
        ('Birthday', 'Birthday'),
        ('Date', 'Date'),
        ('Anniversary', 'Anniversary'),
    )
    name = models.CharField(max_length=20, choices=name_choices, null=True, blank=True)
    decoration_type_choices = (
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Gold'),
    )
    decoration_type = models.CharField(max_length=20, choices=decoration_type_choices, null=True, blank=True)
    decoration_cost = models.FloatField()



class Table(models.Model):
    number = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    number_of_people_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    number_of_people = models.IntegerField(choices=number_of_people_choices, null=True, blank=True)
    check_in = models.DateTimeField(null=True, blank=True)
    
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



