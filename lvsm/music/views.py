from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# home (main) page
def index(request):
    return HttpResponse("<h1>Music page</h1>")


# genre page
# genre_id - shows with what genre we are working now (will be slug type in a future)
def genre(request, genre_id):
    return HttpResponse(f"<h1>Genres</h1><p>{genre_id}</p>")


# year - year of music
def music_year(request, year):
    if int(year) < 1985:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Era of music</h1><p>{year}</p>")


# errors handler function
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Something went wrong, try again later</h1>")
