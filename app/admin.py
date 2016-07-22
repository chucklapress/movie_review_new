from django.contrib import admin
from app.models import Rater
from app.models import Movie
from app.models import Review

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Review)
