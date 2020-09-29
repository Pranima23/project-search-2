import datetime
from reservation.models import Table, Reservation


def check_availability(table, check_in, check_out):
    avail_list = []
    booking_list = Reservation.objects.filter(table=table)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)