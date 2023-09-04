from django.contrib import admin

from music.models import *


class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'photo', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_filter = ['is_published', 'time_create']
    prepopulated_fields = {"slug": ("title",)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Music, MusicAdmin)
admin.site.register(Genre, GenreAdmin)
