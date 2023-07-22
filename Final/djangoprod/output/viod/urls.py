from django.contrib import admin
from django.urls import path, include

from . import views
from .views import profile_view, RegisterView

urlpatterns = [

    path("", views.index, name="vivod"),
    path("main/", views.autocomplete, name="autocomplete"),
    path('main/create/', views.ok_button, name='ok_button'),
    path('profile/',profile_view,name="profile"),
    path('register/',RegisterView.as_view(),name='register'),

]
