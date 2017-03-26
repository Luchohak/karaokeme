from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SongPetition, Song
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def list_songs(request):
    """ View of list of songs
    This view displays all the songs in the library,
    which are the ones the customers can make petitions
    of.
    This view includes a filter for both title and artist
    the filters logic is inside the songlibrary/index.html template.

    """
    # Song objects are ordered by artist.
    queryset_list = Song.objects.all().order_by("artist")
    paginator = Paginator(queryset_list, 30) # Show 30 songs per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "Songs"
    }
    return render(request, 'songlibrary/index.html', context)