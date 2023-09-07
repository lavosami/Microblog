from django.contrib import admin

from music.models import *


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'photo', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_filter = ['is_published', 'time_create']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImageInline]


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name",)}


# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'photo', 'music_id')
#     list_display_links = ('music_id', )
#     search_fields = ('music_id',)


admin.site.register(Music, MusicAdmin)
admin.site.register(Genre, GenreAdmin)
# admin.site.register(Image, ImageAdmin)
