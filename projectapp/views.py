from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.


class HomePView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'Barcha_postlar'


class AboutPView(ListView):
    model = Post
    template_name = 'about.html'
    context_object_name = 'Barcha_postlar'


class ContactPView(ListView):
    model = Post
    template_name = 'about.html'
    context_object_name = 'Barcha_postlar'