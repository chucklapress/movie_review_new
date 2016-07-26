from django.shortcuts import render
from django.db.models import Count, Avg
from app.models import Rater, Movie, Review, Average


# Create your views here.
def index_view(request):
    return render(request, "index.html")

def movie_list(request):

    context = {
       "movies": Movie.objects.all()
    }
    return render(request, "movie.html", context)



def single_view(request,id):

    context = {
        #"movie_id": single_view(),
        "single": Movie.objects.get(id=id)
    }
    return render(request, "single_movie.html", context)

def rater_info(request):

    context = {
        "rater": Review.objects.order_by('rater')[:5],
        "rating": Average.objects.order_by('-number_ratings')[:1]

    }
    return render(request, "rater_information.html",context)

def movie_rating_view(request):

    context = {
        "rated": Average.objects.filter(average=5)

    }
    return render(request, "movie_rated.html", context)

def average_rating(request):
    context = {
    "top_twenty": Average.objects.order_by('-number_ratings')[:20]
    }
    return render(request, "top_twenty.html", context)
