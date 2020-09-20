from django.db import models
from registration.models import Customer


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
        ('Silver', 'Silver'),
    )
    decoration_type = models.CharField(max_length=20, choices=decoration_type_choices, null=True, blank=True)
    decoration_cost = models.FloatField(null=True, blank=True)
    decoration_description = models.TextField(null=True, blank=True)
    event_image = models.ImageField(upload_to = 'event_image', blank=True)

    @staticmethod
    def get_events_by_id(ids):
        return Event.objects.filter(id__in = ids)


class BookEvent(models.Model):
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

