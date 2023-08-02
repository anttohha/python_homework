from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.searchhotels, name="hotels"),
    path('main/', views.autocomplete_hotel, name="autocomplete-hotel"),
    path('main/create/', views.ok_button, name='ok_button'),
    path('main/create/okorder/',views.ok_order,name='orderhotel'),

]