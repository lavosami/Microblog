from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from music.forms import NewPostForm
from music.utils import *


class MusicHome(DataMixin, ListView):
    model = Music
    template_name = 'music/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Music blog")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Music.objects.filter(is_published=True)


class AboutPage(DataMixin, ListView):
    model = Music
    template_name = 'music/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="About the site")
        return dict(list(context.items()) + list(c_def.items()))


class NewPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = NewPostForm
    template_name = 'music/new_post.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="New post")
        return dict(list(context.items()) + list(c_def.items()))


class FeedbackPage(DataMixin, ListView):
    model = Music
    template_name = 'music/feedback.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    return HttpResponse("Login page")


class ShowPost(DataMixin, DetailView):
    model = Music
    template_name = 'music/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class MusicGenre(DataMixin, ListView):
    model = Music
    template_name = 'music/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['posts'][0].genre),
                                      genre_selected=context['posts'][0].genre_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Music.objects.filter(genre__slug=self.kwargs['genre_slug'], is_published=True)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Something went wrong, try again later</h1>")
