from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)

    return render(request, 'movies/index.html', {'movies': movies})

def details(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'movies/details.html', {'movie': movie})
    except Movie.DoesNotExist:
        raise Http404

    # Another shortcut way
    # movie = get_object_or_404(klass=Movie, id=movie_id)
    # return render(request, 'movies/details.html', {'movie': movie})



