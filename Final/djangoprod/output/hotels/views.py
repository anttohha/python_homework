from django.shortcuts import render



# Create your views here.


def searchhotels(request):
    return render(request, "hotels.html")