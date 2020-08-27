from django.db import models
from registration.models import Customer
from events.models import Event


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
    