from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Blog!")

# `code_garden/urls.py` imports `my_blog` — provide a small wrapper so the
# project URL configuration works without raising ImportError. Keep it simple
# for now; we can expand to render templates or list Post objects later.
def my_blog(request):
    return home(request)
