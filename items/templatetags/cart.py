from django import template

register = template.Library()

@register.filter
def cart_quantity(cart_item, cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==cart_item.id:
            print(cart[id])
            return cart[id]
    return 0

@register.filter
def item_total(cart_item, cart):
    return cart_item.price * cart_quantity(cart_item, cart)


@register.filter
def order_total(cart_items, cart):
    sum = 0
    for item in cart_items:
        sum += item_total(item, cart)
    return sum

@register.filter
def event_total(cart_book_events, cart_events):
    sum = 0
    for cart_event in cart_events:
        for event in cart_book_events:
            if int(cart_event) == event.id:
             sum += event.decoration_cost
    return sum


@register.filter(name='is_in_cart')
def is_in_cart(item, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == item.id:
            return True
    return False


@register.filter(name='is_in_cart_events')
def is_in_cart(event, cart_events):
    for id in cart_events:
        if int(id) == event.id:
            return True
    return False




@register.filter(name='first_arg')
def first_arg(cart_book_events, cart_events):
    return cart_book_events, cart_events


@register.filter(name='second_arg')
def second_arg(first_arg, cart_items):
    cart_book_events, cart_events = first_arg
    return cart_book_events, cart_events, cart_items

@register.filter(name='my_filter')
def my_filter(second_arg, cart):
    cart_book_events, cart_events, cart_items = second_arg
    tot1 = event_total(cart_book_events, cart_events)
    tot2 = order_total(cart_items, cart)
    return tot1 + tot2


@register.filter(name="count1")
def count1(cart_events, cart):
    c = 0
    for id in cart_events:
        c=c+1
    keys = cart.keys()
    for id in keys:
        c=c+1
    return c


@register.filter(name="count")
def count(second_arg, cart):
    cart_book_events, cart_events, cart_items = second_arg
    c=0
    for item in cart_items:
        quantity = cart_quantity(item, cart)
        c = c + quantity
    for event in cart_events:
        c = c + 1
    return c

@register.filter(name="count_item")
def count_item(cart_items, cart):
    c=0
    for item in cart_items:
        quantity = cart_quantity(item, cart)
        c = c + quantity
    return c


@register.filter(name="count_event")
def count_event(cart_events):
    c=0
    for event in cart_events:
        c = c + 1
    return c
