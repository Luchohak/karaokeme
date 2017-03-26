from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

from .utils import SONG_MANAGER_GROUP

class SongManager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default='admin')
    username = models.CharField(max_length = 30, default='username')
    password = models.CharField(max_length = 30, default='password')
    first_name = models.CharField(max_length = 30, default='Jhon')
    last_name = models.CharField(max_length = 30, default='Doe')
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """ Override the save method to add the capturista group.
        """
        user_group = Group.objects.get_or_create(name=SONG_MANAGER_GROUP)[0]
        self.user.groups.add(user_group)
        return super(SongManager, self).save(*args, **kwargs)