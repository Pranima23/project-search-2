from django.shortcuts import render, redirect
from django.http import HttpResponse
from registration.models import Customer
from .models import Item, OrderDetails, Order
from events.models import *


# Create your views here.

def index(request):
    
    if request.method == 'POST':
        cart = request.session.get('cart')
        item = request.POST.get('item')
        print('item id:', item)
        new_quantity = int(request.POST.get('quantity'))
        print('quantity ordered:', new_quantity)
        if cart:
            add_newitem_to_cart = {}
            for cart_item in cart:
                if item==cart_item:
                    quantity = int(cart.get(item))
                    print('quantity already in cart:', cart[item])
                    cart[item] = new_quantity
                    print ('updated cart with existing items:', cart)
                elif (item not in cart):
                    add_newitem_to_cart = {}
                    add_newitem_to_cart[item] = new_quantity
                    print('additional item to cart', add_newitem_to_cart)
            if add_newitem_to_cart:
                cart.update(add_newitem_to_cart) 
                print('updated cart with additional items:', cart)
        else:
            cart={}
            cart[item] = new_quantity
            print('new cart:', cart)
        request.session['cart'] = cart
        print(request.session.get('cart'))
        return redirect('/items/menu/')
    
    else:
        print(request.session.get('customer'))
        print(request.session.get('email'))
        items = Item.objects.all()
        if request.session.get('cart') and request.session.get('cart_events'):
            ids = list(request.session.get('cart').keys())
            cart_items = Item.objects.filter(id__in = ids)
            cart_book_events = Event.objects.filter(id__in = request.session.get('cart_events'))
            return render(request, 'menu.html', {'items': items, 'cart_items': cart_items,'cart_book_events': cart_book_events})
        if request.session.get('cart'):
            ids = list(request.session.get('cart').keys())
            cart_items = Item.objects.filter(id__in = ids)
            return render(request, 'menu.html', {'items': items, 'cart_items': cart_items})
        if request.session.get('cart_events'):
            cart_book_events = Event.objects.filter(id__in = request.session.get('cart_events'))
            return render(request, 'menu.html', {'items': items, 'cart_book_events': cart_book_events})
        else:
            return render(request, 'menu.html', {'items': items})
        
            

