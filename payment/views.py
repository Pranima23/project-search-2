from django.shortcuts import render, redirect
from django.http import HttpResponse
from items.models import *
from events.models import *
from registration.models import *
# Create your views here.
def cart(request):
    if request.method=='POST':
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
        return HttpResponse('Nothing to display in cart.')


def pay(request):
    if request.method == 'POST':
        #getting card number
        card_num = request.POST.get('card_num')
        print(card_num)
        #getting customer info
        customer = request.session.get('customer')
        #getting items in cart
        cart = request.session.get('cart')
        #getting events in cart
        cart_events = request.session.get('cart_events')
        events = Event.get_events_by_id(cart_events)
        items = Item.get_items_by_id(list(cart.keys()))
        print('/////////////////////////')
        print(customer, cart, items, events)
        #saving food order to database
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
        for event in events:
            booked_event = BookEvent.objects.create(
                customer = Customer(
                    id = customer
                ),
                event = event
            )
        booked_event.save()
        request.session['cart_events'] = []
        return render(request, 'final.html')
    else:
        return render(request, 'final.html')
