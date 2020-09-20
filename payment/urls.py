from django.urls import path
from . import views

app_name='payment'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('pay/', views.pay, name='pay'),
]