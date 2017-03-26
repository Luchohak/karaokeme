from django.test import TestCase
from django.core.urlresolvers import reverse


class TestPetitionViews(TestCase):
    """Unit test suite for testing the URLs in the app: petition.

    Test the urls for 'petition' which control the creation and deletion of
    song petitions and show the list of petitions.

    """

    def test_petition_creation(self):
        """ Test for the view that shows the petition creation form.
        If the url and template exist the test returns true.
        A 200 http response means the page loaded correctly.

        """
        test_url_name = 'petition:main'
        response = self.client.get(reverse(test_url_name), follow=True)
        self.assertEqual(200, response.status_code)

    def test_petition_deletion(self):
        """ Test for the view that deletes a song petition once the song has been played.
        If the url and template exist the test returns true.
        A 200 http response means the page loaded correctly.

        """
        test_url_name = 'petition:delete'
        response = self.client.get(reverse(test_url_name), follow=True)
        self.assertEqual(200, response.status_code)

    def test_petition_list(self):
        """ Test for the view that shows list of petitions left.
        If the url and template exist the test returns true.
        A 200 http response means the page loaded correctly.

        """
        test_url_name = 'petition:list'
        response = self.client.get(reverse(test_url_name), follow=True)
        self.assertEqual(200, response.status_code)