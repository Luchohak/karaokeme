from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SongPetitionForm
from songlibrary.models import SongPetition
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

def make_petition(request):
    """View make a petition.
    This view uses the SongPetitionForm form 
    to load the data required for making a complete 
    petition.

    """
    form_class = SongPetitionForm
    template_name = 'petition/make_petition'

    if request.method == 'POST':
        petition = SongPetition(song_title=request.user)
        form = SongPetitionForm(request.POST, instance=petition)
        # If all the data has been filled in correctly it saves the petition into the DB
        if form.is_valid():
            form.save()
            # Feedback message telling that the petition has been created
            messages.success(request, "Petition succesfully created")
            return redirect ('petition:list')

    else:
        form = SongPetitionForm()
    return render(request, 'petition/make_petition.html', {'form': form})


def delete_song_petition(request, id):
    """ View to delete a song petition.
    This view calls the delete() method to
    remove a Song Petition from the database

    """
    # instance gets the id from the Song Petition selected
    instance = get_object_or_404(SongPetition, id=id)
    # delete method deletes the instance from the database
    instance.delete()
    # Feedbacj message telling that the petition was deleted 
    messages.success(request, "Petition succesfully deleted")
    return redirect("petition:list")


def list_petitions(request):
    """ View to see the list of petitions.
    This view shows to the song manager and the admin the 
    list of song petitions left. 

    """
    # song petition objects are ordered by date, so the song manager plays the oldest petitions first
    queryset_list = SongPetition.objects.all().order_by("date")
    paginator = Paginator(queryset_list, 5) # Show 5 petitions per page
    
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
        "title": "Song Petitions"
    }
    return render(request, 'petition/petition_list.html', context)
