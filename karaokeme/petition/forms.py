from django import forms
from songlibrary.models import SongPetition

class SongPetitionForm(forms.ModelForm):
    """ Form for making a Song Petition.

    This is the general form for sending a song request to the Song Manager.

    Attributes
    ----------
    song_title = Song title
        Title of the song.
    artist = Artist
        Artist of the song.
    performers = Performers
        Members of the table that are going to perform the song.
    table = Table
        Table number of the performers.
    """
    class Meta:
        model = SongPetition
        fields = ['song_title', 'artist', 'performers', 'table']
