from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from music.forms import NewPostForm
from music.models import Music, Genre

menu = [
    {'title': "About a site", 'url_path': "about"},
    {'title': "Create a post", 'url_path': "new_post"},
    {'title': "Feedback", 'url_path': "feedback"},
    {'title': "Sign In", 'url_path': "login"}
]


# home (main) page
def index(request):
    posts = Music.objects.all()

    args = {
        'title': 'Music blog',
        'menu': menu,
        'posts': posts,
        'genre_selected': 0
    }
    return render(request, 'music/index.html', context=args)


def about(request):
    return render(request, 'music/about.html', {'title': 'About a site', 'actions': menu})


# genre page
# genre_id - shows with what genre we are working now (will be slug type in a future)
def genre(request, genre_id):
    return HttpResponse(f"<h1>Genres</h1><p>{genre_id}</p>")


# year - year of music
def music_year(request, year):
    if int(year) < 1985:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Era of music</h1><p>{year}</p>")


def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = NewPostForm()

    return render(request, 'music/new_post.html', {'form': form, 'menu': menu, 'title': 'New post'})


def feedback(request):
    return HttpResponse("Feedback page")


def login(request):
    return HttpResponse("Login page")


def show_post(request, post_slug):
    post = get_object_or_404(Music, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'genre_selected': post.genre_id,
    }

    return render(request, 'music/post.html', context=context)


def show_genre(request, genre_id):
    posts = Music.objects.filter(genre_id=genre_id)

    if len(posts) == 0:
        raise Http404()

    args = {
        'title': 'Genres',
        'menu': menu,
        'posts': posts,
        'genre_selected': genre_id
    }
    return render(request, 'music/index.html', context=args)


# error 404 handler function
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Something went wrong, try again later</h1>")
