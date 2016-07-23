from django.contrib import admin
from app.models import Rater
from app.models import Movie
from app.models import Review
from app.models import Average

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Average)
