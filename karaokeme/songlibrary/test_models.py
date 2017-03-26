from django.test import TestCase
from .models import Song, SongPetition
import datetime


class TestSongPetition(TestCase):
    """ Unit test suite for testing the SongPetition model in .models
    """

    def setUp(self):
        """ Setup required for the tests in this suite.

        """
        SongPetition.objects.create(song_title='Crazy',
                                    artist='Aerosmith',
                                    performers='Allan',
                                    table=2
                                    )

    def test_str(self):
        """ Checks that this method __str__ method returns the name
        of the object.
        """
        petition = SongPetition.objects.get(song_title='Crazy')
        self.assertEqual(str(petition), 'Crazy')

class TestSong(TestCase):
    """ Unit test suite for testing the Song model in .models
    """

    def setUp(self):
        """ Setup required for the tests in this suite.

        """
        Song.objects.create(song_title='Still Got The Blues',
                            artist='Gary Moore',
                                    )

    def test_str(self):
        """ Checks that this method __str__ method returns the name
        of the object.
        """
        song = Song.objects.get(song_title='Still Got The Blues')
        self.assertEqual(str(song), 'Still Got The Blues')
