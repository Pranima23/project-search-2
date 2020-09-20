from django.shortcuts import render, redirect
from .models import Event

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
        return render(request, 'events.html', {'events': events})