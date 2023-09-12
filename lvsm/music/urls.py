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
    path('about/', AboutPage.as_view(), name='about'),
    path('new_post/', NewPost.as_view(), name='new_post'),
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('genre/<slug:genre_slug>/', MusicGenre.as_view(), name='genre')
]
