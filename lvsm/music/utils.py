from django.db.models import Count

from .models import *

menu = [
    {'title': "About a site", 'url_path': "about"},
    {'title': "Create a post", 'url_path': "new_post"},
    {'title': "Feedback", 'url_path': "feedback"},
    {'title': "Sign In", 'url_path': "login"}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        genres = Genre.objects.annotate(Count('music'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu

        context['genres'] = genres
        if 'genre_selected' not in context:
            context['genre_selected'] = 0
        return context
