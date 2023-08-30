from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Music page</h1>")


def genre(request, genre_id):
    return HttpResponse(f"<h1>Genres</h1><p>{genre_id}</p>")


def musicYear(request, year):
    return HttpResponse(f"<h1>Era of music</h1><p>{year}</p>")
