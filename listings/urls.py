from django.urls import path

from . import views

urlpatterns = [
    path('', views.vault, name='vault'),
    path('vault/<int:listing_id>/', views.cupcake, name='cupcake')
]