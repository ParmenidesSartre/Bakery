from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('checkout/', views.checkout, name='cart_checkout'),
    path('checkout/success', views.success , name='success')
]
