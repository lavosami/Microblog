from django.urls import path

from .views import *

"""
App's pages:
    home (main page with link etc.)
    genre (posts about music sorted by genre)
    music_year (posts about music sorted by release year)
"""
urlpatterns = [
    path('', MusicHome.as_view(), name='home'),
    # path('', index, name='home'),
    path('about/', about, name='about'),
    path('new_post/', NewPost.as_view(), name='new_post'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('genre/<slug:genre_slug>/', MusicGenre.as_view(), name='genre')
]
