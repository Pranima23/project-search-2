from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'menu.html', {'items': items})

def add(request):
    return render(request, 'add.html')

def result(request):
    result=int(request.POST['num1']) + int(request.POST['num2'])
    return render(request, 'result.html', {'result': result})
