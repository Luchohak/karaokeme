from . import views
from django.conf.urls import url, include
from .views import login_view, logout_view

app_name = 'administration'
""" URLs for app: 'administration'.

URLs
--------
Register: administration/register 
    Loads the UserFormView form as a view to create a new user.
Login: administration/login 
    Loads the login_view view to login a user.
Logout: administration/logout
    Loads the logout_view which contains the logout() method, this view is never displayed.

"""
urlpatterns = [
    url(r'register/$', views.UserFormView.as_view(), name = 'register'),
    url(r'login/$', login_view, name = 'login'),
    url(r'logout/$', logout_view, name = 'logout'),
]
