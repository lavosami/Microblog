from django.urls import path, re_path

from .views import *

"""
App's pages:
    home (main page with link etc.)
    genre (posts about music sorted by genre)
    music_year (posts about music sorted by release year)
"""
urlpatterns = [
    path('', index, name='home'),
    path('genre/<int:genre_id>/', genre),
    re_path(r'^music_year/(?P<year>[0-9]{4})/', music_year)
]
