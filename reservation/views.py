from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table, Reservation
from registration.models import Customer
from .reservation_function.availability import check_availability
from .form import AvailabilityForm
from django.contrib import messages
from registration.middlewares.auth import auth_middleware


@auth_middleware
# Create your views here.
def reservation(request):
    
    if request.method=='POST':
        customer = request.session.get('customer')
        no_of_people = (request.POST.get('no_of_people'))
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        table_list = Table.objects.filter(capacity=no_of_people)
        print(table_list)

        for table in table_list:
            print(table)

        available_tables = []
        for table in table_list:
            if check_availability(table, data['check_in'], data['check_out']):
                available_tables.append(table)

        if len(available_tables) > 0:
            print ('Table available')
            table = available_tables[0]
            booking = Reservation.objects.create(
                customer=Customer(
                    id = customer
                ),
                table=table,
                number_of_people=no_of_people,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()         
            
            print(no_of_people, data['check_in'], data['check_out'])
            return render(request, 'goback.html')
        else:           
            return render(request, 'comein.html')
    else:
        return render(request, 'reservation1.html')