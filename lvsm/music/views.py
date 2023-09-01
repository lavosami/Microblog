from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from music.models import Music

actions = ["About a site", "Create new post", "Feedback", "Sign In"]


# home (main) page
def index(request):
    posts = Music.objects.all()
    return render(request, 'music/index.html', {'title': 'Music blog', 'actions': actions, 'posts': posts})


def about(request):
    return render(request, 'music/about.html', {'title': 'About a site', 'actions': actions})


# genre page
# genre_id - shows with what genre we are working now (will be slug type in a future)
def genre(request, genre_id):
    return HttpResponse(f"<h1>Genres</h1><p>{genre_id}</p>")


# year - year of music
def music_year(request, year):
    if int(year) < 1985:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Era of music</h1><p>{year}</p>")


# error 404 handler function
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Something went wrong, try again later</h1>")
