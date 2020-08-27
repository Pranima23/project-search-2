from django.db import models


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