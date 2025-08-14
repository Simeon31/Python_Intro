from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_year', 'daily_rate')
    list_filter = ('release_year',)

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

