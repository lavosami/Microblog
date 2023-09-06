from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from music.forms import NewPostForm
from music.models import *

menu = [
    {'title': "About a site", 'url_path': "about"},
    {'title': "Create a post", 'url_path': "new_post"},
    {'title': "Feedback", 'url_path': "feedback"},
    {'title': "Sign In", 'url_path': "login"}
]


class MusicHome(ListView):
    model = Music
    template_name = 'music/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Music blog'
        context['genre_selected'] = 0
        return context

    def get_queryset(self):
        return Music.objects.filter(is_published=True)


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


class NewPost(CreateView):
    form_class = NewPostForm
    template_name = 'music/new_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'New post'
        return context


def feedback(request):
    return HttpResponse("Feedback page")


def login(request):
    return HttpResponse("Login page")


class ShowPost(DetailView):
    model = Music
    template_name = 'music/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post'].title

        return context


class MusicGenre(ListView):
    model = Music
    template_name = 'music/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['posts'][0].genre)
        context['genre_selected'] = context['posts'][0].genre_id
        return context

    def get_queryset(self):
        return Music.objects.filter(genre__slug=self.kwargs['genre_slug'], is_published=True)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Something went wrong, try again later</h1>")
