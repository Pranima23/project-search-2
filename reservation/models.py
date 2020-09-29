from django.db import models
from registration.models import Customer
from events.models import Event


class Table(models.Model):
    table_choices=(
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10))
    table_number = models.IntegerField(choices=table_choices,null=True, blank=True)
    #table_number = models.IntegerField(null=True, blank=True)
    capacity_choices=(
        (2,2),
        (4,4),
        (6,6),
        (8,8),
        (10,10)
    )
    capacity = models.IntegerField(choices=capacity_choices, null=True, blank=True)


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
    check_out = models.DateTimeField(null=True, blank=True)
    