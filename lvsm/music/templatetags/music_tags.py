from django import template
from music.models import *

register = template.Library()


@register.simple_tag()
def get_genres(filter=None):
    if not filter:
        return Genre.objects.all()
    else:
        return Genre.objects.filter(pk=filter)


@register.inclusion_tag("music/list_genres.html")
def show_genres(sort=None, genre_selected=0):
    if not sort:
        genre = Genre.objects.all()
    else:
        genre = Genre.objects.order_by(sort)
    return {"genre": genre, "genre_selected": genre_selected}


@register.inclusion_tag("music/slider_photo.html")
def show_photos(music_id):
    photos = Image.objects.filter(music_id=music_id)
    return {"photos": photos}
