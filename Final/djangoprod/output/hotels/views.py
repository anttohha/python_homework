import json
import ast

from ast import keyword
from amadeus import Client, ResponseError, Location
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import addFormHotel


# Create your views here.
amadeus = Client(
    client_id='H3mCtiSJ944pFTWEhdd5Nr1hoGJDYGzy',
    client_secret='wVRZx2RJuXr8EWkn'
)

def searchhotels(request):
    return render(request, "hotels.html")




def get_hotel_list(data):
    result = []
    for i, val in enumerate(data):
        result.append(data[i]["iataCode"] + ", " + data[i]["name"])
    result = list(dict.fromkeys(result))
    return json.dumps(result)


def autocomplete_hotel(request):
    form = addFormHotel()

    if 'term' in request.GET:
        data = amadeus.reference_data.locations.get(
            keyword=request.GET.get("term", None), subType=Location.ANY
        ).data

        print(len(data))

        return HttpResponse(get_hotel_list(data), "application/json")

    else:
        context = {

            'form': form,

        }
    return render(request, 'hotels.html', context)




def ok_button(request):
    if request.method == "POST":
        someform = addFormHotel(request.POST)
        if someform.is_valid:
            flight_date = request.POST.get("data_incoming")
            flight_date_reverse = request.POST.get("data_outcomming")
            flyfromcity = request.POST.get("hotelplace")

            print(flight_date)
            print(flight_date_reverse)
            print(flyfromcity)


            codeairport_sub = flyfromcity.split(',')

            codeairport = codeairport_sub[0]


            hotel_list = amadeus.reference_data.locations.hotels.by_city.get(cityCode= codeairport_sub[0])
            print("--------------------------")
            print(hotel_list[0].data)

        content = {
            "flight_date": flight_date,
            "flight_date_reverse": flight_date_reverse,
            "flyfromcity": flyfromcity,


        }

    return render(request, 'test1223.html', context=content)
