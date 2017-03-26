from django.test import TestCase
from django.core.urlresolvers import reverse


class TestAdminViews(TestCase):
    """Unit test suite for testing the URLs in the app: administration.

    Test the urls for 'administration' which control the creation, login and logout
    of users.

    """

    def test_user_registration(self):
        """ Test for the view that shows the registration form.
        If the url and template exist the test returns true.
        A 200 http response means the page loaded correctly.

        """
        test_url_name = 'administration:register'
        response = self.client.get(reverse(test_url_name), follow=True)
        self.assertEqual(200, response.status_code)

    def test_user_login(self):
        """ Test for the view that shows the login form.
        If the url and template exist the test returns true.
        A 200 http response means the page loaded correctly.

        """
        test_url_name = 'administration:login'
        response = self.client.get(reverse(test_url_name), follow=True)
        self.assertEqual(200, response.status_code)

    def test_user_logout(self):
        """ Test for the view that logs out the user.
        If the url and template exist the test returns true.
        A 200 http response means the page loaded correctly.

        """
        test_url_name = 'administration:logout'
        response = self.client.get(reverse(test_url_name), follow=True)
        self.assertEqual(200, response.status_code)
