from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from songlibrary.models import Song
from . import views
from .views import list_songs

app_name='songlibrary'
""" URLs for app: 'songlibrary'.

URLs
--------
List: songlibrary/
    Loads the list_songs view to show the query of all the songs registered in the system.
    This view contains pagination and a filter for finding songs faster.

"""
urlpatterns = [ 
    url(r'^$', list_songs, name='list'),
]