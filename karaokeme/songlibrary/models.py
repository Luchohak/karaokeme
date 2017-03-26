from __future__ import unicode_literals

from django.db import models


class SongPetition(models.Model):
    """ Song Petition model.

    This is the model for creating song petitions.

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
    date = Date
        Date on which the petition was made, this is auto created,
        the user is not allowed to specify the date.
    """
    song_title = models.CharField(max_length = 30)
    artist = models.CharField(max_length = 30)
    performers = models.CharField(max_length = 50)
    table = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_title

class Song(models.Model):
    """ Song model.

    This is the general form for sending a song request to the Song Manager.

    Attributes
    ----------
    song_title = Song title
        Title of the song.
    artist = Artist
        Artist of the song.
    """
    song_title = models.CharField(max_length = 30)
    artist = models.CharField(max_length = 30)

    def __str__(self):
        return self.song_title