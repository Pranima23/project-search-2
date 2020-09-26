from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    print(request.session.get('email'))
    return render(request, 'index.html')
    
    
def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       

        if password1==password2:
            if Customer.objects.filter(email=email).exists():
                print('email already exists')
                messages.info(request, 'Email already exists!')
                return redirect('/signup/')                
            else:
                customer = Customer.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password1,
                )
                customer.save()
            return redirect('/login/')  
        else:
            messages.info(request, 'Password not matched!')
            return redirect('/signup/')   

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        #getting login credentials
        email = request.POST['email']
        password = request.POST['password']

        #checking if email is in database
        if not Customer.objects.get(email=email):
            customer = None
        else:
            customer = Customer.objects.get(email=email)
        if customer:
            #checking if password matches
            if password == customer.password:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                print(request.session['email'])
                print(request.session['customer'])
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password!')
                return redirect('login')
        if not customer:
            messages.error(request, 'Invalid email or password!')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('login')


