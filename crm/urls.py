from django.contrib import admin
from django.urls import path
from .  import views   #new


urlpatterns = [
    path('',views.home),
    path('customer/<str:pk>/',views.customer),
    path('products/',views.products),
]