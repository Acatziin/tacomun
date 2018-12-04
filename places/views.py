from django.shortcuts import render
from django.http import HttpResponse
from .models import Place

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        user_places = user.place_set.all()
        context = {
            'places' : user_places
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')

def detail_place(request, place_id):
    user = request.user
    place = user.place_set.get(id=place_id)
    context = {
        'place' : place
    }
    return render(request, 'detail.html', context)
        