from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from music.forms import NewPostForm, RegisterUserForm, LoginUserForm
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
        return Music.objects.filter(is_published=True).select_related('genre')


class AboutPage(DataMixin, ListView):
    paginate_by = 10
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
    paginate_by = 10
    model = Music
    template_name = 'music/feedback.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        return dict(list(context.items()) + list(c_def.items()))


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
        g = Genre.objects.get(slug=self.kwargs['genre_slug'])
        c_def = self.get_user_context(title=str(g.name),
                                      genre_selected=g.pk)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Music.objects.filter(genre__slug=self.kwargs['genre_slug'], is_published=True).select_related('genre')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Something went wrong, try again later</h1>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'music/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign Up")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'music/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_user_context(**kwargs)
        c_def = self.get_user_context(title='Sign In')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
