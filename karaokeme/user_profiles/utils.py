
ADMIN_GROUP = 'admin'
SONG_MANAGER_GROUP = 'songmanager'

def is_member(user, groups):
    """ Test if a user belongs to any of the groups provided.

    This function is meant to be used by the user_passes_test decorator to control access
    to views.

    Parameters
    ----------
    user : django.contrib.auth.models.User
        The user which we are trying to identify that belongs to a certain group.
    groups : list of str
        A list of the groups we are checking if the user belongs to.

    Returns
    ---------
    bool
        True if the user belongs to any of the groups. False otherwise
    """
    return any(map(lambda g: user.groups.filter(name=g).exists(), groups))


def is_admin(user):
    """ Test if a user has the capturista group.

    This function is meant to be used by the user_passes_test decorator to control access
    to views. It uses the is_member function with a predefined list of groups.

    Parameters
    ----------
    user : django.contrib.auth.models.User
        The user which we are trying to identify that belongs to capturista.

    Returns
    ---------
    bool
        True if the user has capturista as a group.
    """
    return is_member(user, [ADMIN_GROUP])


def is_song_manager(user):
    """ Test if a user has the capturista group.

    This function is meant to be used by the user_passes_test decorator to control access
    to views. It uses the is_member function with a predefined list of groups.

    Parameters
    ----------
    user : django.contrib.auth.models.User
        The user which we are trying to identify that belongs to capturista.

    Returns
    ---------
    bool
        True if the user has capturista as a group.
    """
    return is_member(user, [SONG_MANAGER_GROUP])