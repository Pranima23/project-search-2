from django.shortcuts import render, redirect
from .models import Event
from items.models import Item

# Create your views here.
def event(request):
    if request.method=='POST':
        print('added to cart')
        cart_events = request.session.get('cart_events')
        event = request.POST.get('event')
        if cart_events:
            cart_events.append(event)
        else:
            cart_events = [event]
        print('view:', event)        
        request.session['cart_events'] = cart_events
        print('view:', request.session.get('cart_events'))
        return redirect('/events/')
    else:
        events = Event.objects.all()
        if request.session.get('cart') and request.session.get('cart_events'):
            ids = list(request.session.get('cart').keys())
            cart_items = Item.objects.filter(id__in = ids)
            cart_book_events = Event.objects.filter(id__in = request.session.get('cart_events'))
            return render(request, 'events.html', {'events': events, 'cart_items': cart_items,'cart_book_events': cart_book_events})
        if request.session.get('cart'):
            ids = list(request.session.get('cart').keys())
            cart_items = Item.objects.filter(id__in = ids)
            return render(request, 'events.html', {'events': events, 'cart_items': cart_items})
        if request.session.get('cart_events'):
            cart_book_events = Event.objects.filter(id__in = request.session.get('cart_events'))
            return render(request, 'events.html', {'events': events, 'cart_book_events': cart_book_events})
        else:
            return render(request, 'events.html', {'events': events})