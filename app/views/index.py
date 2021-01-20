from django.views.generic import TemplateView
from .top_rated_movies import movies
from django.shortcuts import render, redirect
import random


def index(request):
    context = {}
    random.shuffle(movies)
    context["movies"] = movies[:6]
    return render(request, "index.html", context)

class about_us(TemplateView):
    template_name = "about_us.html"

