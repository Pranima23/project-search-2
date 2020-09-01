from django.urls import path
from . import views

app_name='items'

urlpatterns = [
    path('menu/', views.index, name='menu'),
    path('cart/', views.cart, name='cart'),
]