import json
import ast
from amadeus import Client, ResponseError, Location
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import addForm, RegisterForm

# Create your views here.
from viod.models import Product



amadeus = Client(
    client_id='H3mCtiSJ944pFTWEhdd5Nr1hoGJDYGzy',
    client_secret='wVRZx2RJuXr8EWkn'
)


def get_city_airport_list(data):
    result = []
    for i, val in enumerate(data):
        result.append(data[i]["iataCode"] + ", " + data[i]["name"])
    result = list(dict.fromkeys(result))
    return json.dumps(result)


def autocomplete(request):
    form = addForm()

    if 'term' in request.GET:
        data = amadeus.reference_data.locations.get(
            keyword=request.GET.get("term", None), subType=Location.ANY
        ).data

        print(len(data))
        return HttpResponse(get_city_airport_list(data), "application/json")

    else:
        context = {

            'form': form,

        }
    return render(request, 'core/home.html', context)


def ok_button(request):
    if request.method == "POST":
        someform = addForm(request.POST)
        if someform.is_valid:
            flight_date = request.POST.get("flight_date")
            flight_date_reverse = request.POST.get("flight_date_reverse")
            flyfromcity = request.POST.get("flyfromcity")
            flytocity = request.POST.get("flytocity")
            cabine = request.POST.get("cabine")
            print(flight_date)
            print(flight_date_reverse)
            print(flyfromcity)
            print(flytocity)
            print(cabine)

            codeairport_sub = flyfromcity.split(',')
            codeairportend_sub = flytocity.split(',')
            codeairport_start = codeairport_sub[0]
            codeairport_end = codeairportend_sub[0]

            flights = amadeus.shopping.flight_offers_search.get(originLocationCode=codeairport_start,
                                                                destinationLocationCode=codeairport_end,
                                                                departureDate=flight_date, adults=1,
                                                                travelClass=cabine).data

            print(flights[0])


            dataa = []
            k1 = len(flights)
            for i in range(0, k1):
                dataa.append(
                    (flights[i].get("id"),
                     flights[i].get("itineraries")[0].get("segments")[0].get("departure").get("at"),
                     flights[i].get("itineraries")[0].get("segments")[0].get("arrival").get("at"),
                     flights[i].get("price").get("currency"),
                     flights[i].get("price").get("total"), flights[i].get("itineraries")[0].get("duration")))

            new_dict = {}
            for i in range(0, k1):
                new_dict[i] = [
                    flights[i].get("id"),
                    flights[i].get("itineraries")[0].get("segments")[0].get("departure").get("at"),
                    flights[i].get("itineraries")[0].get("segments")[0].get("arrival").get("at"),
                    flights[i].get("price").get("currency"),
                    flights[i].get("price").get("total"),
                    flights[i].get("itineraries")[0].get("duration")

                ]

        #print(new_dict)

        content = {
            "flight_date": flight_date,
            "flight_date_reverse": flight_date_reverse,
            "flyfromcity": flyfromcity,
            "flytocity": flytocity,
            "flights_data": flights,
            "cabine": cabine,
            "dataa": dataa,
            "dict1": new_dict,
        }

    return render(request, 'core/test1223.html', context=content)



def index(request):
    return render(request, "default.html")


@login_required
def profile_view(request):
    return render(request,'loguser/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)