from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'menu.html', {'items': items})