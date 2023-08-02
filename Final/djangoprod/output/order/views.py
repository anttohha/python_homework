from django.shortcuts import render

from .forms import addformorderhotel


# Create your views here.


def orderhotel(request):
    form = addformorderhotel()
    contex = {
        'form': form,
    }
    return render(request, "hotel/orderhotel.html",contex)




