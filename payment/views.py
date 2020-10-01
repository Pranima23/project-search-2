from django.shortcuts import render, redirect
from django.http import HttpResponse
from items.models import Item, Order, OrderDetails
from events.models import Event, BookEvent
from registration.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from registration.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

# Create your views here.
def cart(request):
    if request.method=='POST':
        #to submit feedback form
        if request.POST.get('todo')=='form':
            message = request.POST.get('msg')            
            send_mail('Feedback',
            message,            
            settings.EMAIL_HOST_USER, 
            ['reservendine2020@gmail.com'],           
            fail_silently=False)
            return redirect('/payment/cart/')
        #to remove item from cart
        elif request.POST.get('todo') == 'remove':
            cart = request.session.get('cart')
            remove_item = request.POST.get('item')
            if cart:
                if remove_item:
                    cart.pop(remove_item)
                    request.session['cart'] = cart
            remove_event = request.POST.get('event')
            cart_events = request.session.get('cart_events')
            if cart_events:
                if remove_event:
                    cart_events.remove(remove_event)
                    request.session['cart_events'] = cart_events
        #to alter quantity of item in cart
        else:
            item = request.POST.get('item')
            minus = request.POST.get('minus')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(item)
                if quantity:
                    if minus:
                        if quantity<=1:
                            cart.pop(item)
                        else:
                            cart[item]  = quantity-1
                    else:
                        cart[item]  = quantity+1
            request.session['cart'] = cart
            print('cart' , request.session['cart'])
        return redirect('/payment/cart/')
        
        

    elif request.session.get('cart') and request.session.get('cart_events'):
        print('Event: ', request.session.get('cart_events'))
        ids = list(request.session.get('cart').keys())
        print(ids)
        cart_items = Item.objects.filter(id__in = ids)
        print (cart_items)
        cart_book_events = Event.objects.filter(id__in = request.session.get('cart_events'))
        print(cart_book_events)
        return render(request, 'cart.html', {'cart_items': cart_items,'cart_book_events': cart_book_events})
    elif request.session.get('cart'):
        ids = list(request.session.get('cart').keys())
        print(ids)
        cart_items = Item.objects.filter(id__in = ids)
        print (cart_items)
        return render(request, 'cart.html', {'cart_items': cart_items})
    elif request.session.get('cart_events'):
        cart_book_events = Event.objects.filter(id__in = request.session.get('cart_events'))
        print(cart_book_events)
        return render(request, 'cart.html', {'cart_book_events': cart_book_events})
    else:
        return render(request, 'cart.html')

@auth_middleware
def pay(request):
    
    if request.method == 'POST':
        #getting customer info
        customer = request.session.get('customer')
        #getting items in cart
        cart = request.session.get('cart')
        if cart:
            items = Item.get_items_by_id(list(cart.keys()))
            #saving ordered food to database
            order = Order(
                customer = Customer(
                    id = customer
                )
            )
            order.save()
            for item in items:
                order_details = OrderDetails(
                    order = order,
                    item = item,
                    quantity = cart.get(str(item.id))
                )
                print(order_details.save())
            request.session['cart'] = {}
        #getting events in cart
        cart_events = request.session.get('cart_events')
        if cart_events:
            events = Event.get_events_by_id(cart_events)
            items = Item.get_items_by_id(list(cart.keys()))
            #saving booked event to database
            for event in events:
                booked_event = BookEvent.objects.create(
                    customer = Customer(
                        id = customer
                    ),
                    event = event
                )
            booked_event.save()
            request.session['cart_events'] = []
        messages.info(request, "Your order has been saved!")
        return render(request, 'final.html')
    else:
        
        return render(request, 'final.html')
