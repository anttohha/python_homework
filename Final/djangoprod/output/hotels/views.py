import json
import ast
import time
import folium

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
from .formorder_hotel import addformorderhotel

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

            citycode = codeairport_sub[0]

            hotel_list = amadeus.reference_data.locations.hotels.by_city.get(cityCode=citycode).data

            dict_hotel = {}
            map = folium.Map(location=[50.4512, -104.6166], tiles='cartodbpositron', zoom_start=4)
            for i in range(len(hotel_list)):

                code1 = hotel_list[i]['hotelId']

                hotels_by_city = amadeus.shopping.hotel_offers_search.get(hotelIds=code1, adults='1',
                                                                          checkInDate=flight_date,
                                                                          checkOutDate=flight_date_reverse).data

                if len(hotels_by_city) > 0:
                    print(code1)
                    print(f'название отеля- ', hotel_list[i]['name'])
                    print(f'общая стоимость- ', hotels_by_city[0]['offers'][0]['price']['total'])
                    dict_hotel[i] = [
                        hotel_list[i]['name'],
                        hotels_by_city[0]['offers'][0]['price']['total'],
                        hotels_by_city[0]['offers'][0]['id'],
                        folium.Marker([hotels_by_city[0]['hotel']['latitude'], hotels_by_city[0]['hotel']['longitude']],
                                      popup=hotel_list[i]['name']).add_to(map)
                    ]
                time.sleep(1)

        # folium.Marker([49.00315, 2.52003]).add_to(map)
        # folium.Marker([49.00984, 2.55405]).add_to(map)
        # folium.Marker([48.9911, 2.51526]).add_to(map)
        folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
        folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
        folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
        folium.LayerControl().add_to(map)

        map = map._repr_html_()

        content = {
            "flight_date": flight_date,
            "flight_date_reverse": flight_date_reverse,
            "flyfromcity": flyfromcity,
            "dict_hotel": dict_hotel,
            'map': map,

        }
    return render(request, 'test1223.html', context=content)


def ok_order(request):
    if request.method == "POST":
        form2 = addformorderhotel()
        id = request.POST.get("id")

        print(id)
        offer_availability = amadeus.shopping.hotel_offer_search(id).get().data

        datain = offer_availability['offers'][0]['checkInDate']
        dataout = offer_availability['offers'][0]['checkOutDate']
        categoryroom = offer_availability['offers'][0]['room']['typeEstimated']['category']
        beds = offer_availability['offers'][0]['room']['typeEstimated']['beds']
        bedstype = offer_availability['offers'][0]['room']['typeEstimated']['bedType']
        typeprice = offer_availability['offers'][0]['price']['currency']
        pricetotal = offer_availability['offers'][0]['price']['total']

        print(offer_availability['offers'][0]['checkInDate'])
        print(offer_availability['offers'][0]['checkOutDate'])
        print(offer_availability['offers'][0]['room']['typeEstimated']['category'])
        print(offer_availability['offers'][0]['room']['typeEstimated']['beds'])
        print(offer_availability['offers'][0]['room']['typeEstimated']['bedType'])
        print(offer_availability['offers'][0]['price']['currency'])
        print(offer_availability['offers'][0]['price']['total'])
        print(offer_availability['offers'][0]['policies']['guarantee']['acceptedPayments']['methods'])

        contex = {
            'form': form2,
            'id': id,
            'datain': datain,
            'dataout': dataout,
            'categoryroom': categoryroom,
            'beds': beds,
            'bedstype': bedstype,
            'typeprice': typeprice,
            'pricetotal': pricetotal,

        }

    return render(request, 'order/orderhotel.html', context=contex)
