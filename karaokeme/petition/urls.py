from django.conf.urls import url
from .views import make_petition, delete_song_petition, list_petitions
from django.views.generic import ListView
from songlibrary.models import SongPetition

app_name = 'petition'
""" URLs for app: 'petition'.

URLs
--------
Request: petition/request
    Loads the make_petition view to create a new petition.
Delete: petition/delete
    Loads the delete_song_petition view to delete a petition when the song has been played.
List: petition/request-list
    Loads the list_petitions view to show the list of petitions left.

"""
urlpatterns = [ 
    url(r'^request/', make_petition, name='main'),
    url(r'^(?P<id>\d+)/delete/', delete_song_petition, name='delete'),
    url(r'^request-list/', list_petitions, name='list'),
]
