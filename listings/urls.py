from django.urls import path

from . import views

urlpatterns = [
    path('', views.vault, name='vault'),
    path('vault/<slug:name>/', views.cupcake, name='cupcake')
]