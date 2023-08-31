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
    path('about/', about, name='about')
]
