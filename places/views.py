from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Place, EvalPlace
from .forms import PlaceForm, EvaluationForm

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

def create_place(request):
    if request.user.is_authenticated:
        form = PlaceForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                place = form.save(commit = False)
                place.user = request.user
                place.save()
                return redirect('index')
        return render(request, 'create_place.html', {'form':form})  
    else:
        return redirect('login')

def edit_place(request, place_id):
    place = Place.objects.get(id=place_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PlaceForm(request.POST, instance=place)
            if form.is_valid():
                place = form.save(commit = False)
                place.save()
                return redirect('index')
        else:
            form = PlaceForm(instance=place)
        return render(request, 'edit_place.html', {'form':form})  
    else:
        return redirect('login')


def delete_place(request, place_id):
    place = Place.objects.get(id=place_id)
    if request.user.is_authenticated:
        place.delete()
        return render(request, 'delete_place.html')
    else:
        return redirect('login')

def add_evaluation(request, place_id):
    if request.user.is_authenticated:
        form = EvaluationForm(request.POST or None)
        place = Place.objects.get(id=place_id)
        if request.method == 'POST':
            if form.is_valid():
                evaluation = form.save(commit = False)
                evaluation.user = request.user
                evaluation.place = place
                evaluation.save()
                return redirect('index')
        return render(request, 'add_evaluation.html', {'form':form})  
    else:
        return render(request, 'home.html')