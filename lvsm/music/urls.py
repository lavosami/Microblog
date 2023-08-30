from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('genre/<int:genre_id>/', genre),
    re_path(r'^music_year/(?P<year>[0-9]{4})/', musicYear)
]