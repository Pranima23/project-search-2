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
    for event in cart_events:
        if int(event) == cart_book_events.id:
             sum += cart_book_events.decoration_cost
    return sum