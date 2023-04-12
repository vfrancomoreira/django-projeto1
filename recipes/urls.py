from django.urls import path

from . import views


def home(request):
    return path(request, views.home)
