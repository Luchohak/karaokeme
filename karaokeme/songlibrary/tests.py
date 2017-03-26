from django.test import TestCase
from django.core.urlresolvers import reverse


class TestLibraryViews(TestCase):
    """Unit test suite for testing the URLs in the app: songlibrary.

    Test the urls for 'songlibrary' which display the songs registered in the system.

    """

    def test_reinscription_studies(self):
        """ Test for the view that shows the list of songs.
        If the url and template exist the test returns true.
        A 200 http response means the page loaded correctly.

        """
        test_url_name = 'songlibrary:list'
        response = self.client.get(reverse(test_url_name), follow=True)
        self.assertEqual(200, response.status_code)
