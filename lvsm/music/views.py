from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Music page</h1>")


def categories(request):
    return HttpResponse("<h1>Categories</h1>")
