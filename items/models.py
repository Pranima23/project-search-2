from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 50)
    price = models.FloatField()
    about_item = models.TextField()
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='item_image', blank=True)
    item_type_choices = (
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Drinks', 'Drinks'),
    )
    item_type = models.CharField(max_length = 20, choices = item_type_choices, default = '')
