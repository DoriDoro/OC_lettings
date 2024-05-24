"""
Model for managing user profiles in the application.

This module defines the :class:`lettings.Profile` model, which represents user profiles in the
application. Each Profile is associated with a corresponding :class:`User` model instance,
establishing a one-to-one relationship between users and their profiles.

Model:
    - Profile: Represents a :class:`User` instance with a favourite_city.

Methods:
    - __str__(): Returns a string representation of the :class:`profile.Profile`, which is the
      username of the associated user.

Usage:
    The Profile model can be used to store additional information about users beyond what is
    provided by the built-in User model. In this :class:`profile.Profile` is just a favorite_city
    added.

Example:
    To create a new user profile:
        user = User.objects.create(username='example_user', ...)
        profile = Profile.objects.create(user=user, favorite_city='New York')

:param User: Import the built-in User model from Django's authentication framework.
:param models: Import Django's database models module.
"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Model for managing user profiles in the application.

    Represents user profiles in the application, associated with corresponding :class:`User` model
    instances.

    Methods:
        - __str__(): Returns a string representation of the :class:`profile.Profile`.

    Usage:
        The :class:`profile.Profile` model can be used to store additional information about users
        beyond what is provided by the built-in :class:`User` model.

    Example:
        To create a new user profile:
            user = User.objects.create(username='example_user', ...)
            profile = Profile.objects.create(user=user, favorite_city='New York')

    :param user: A one-to-one relationship with the :class:`User` model, linking each profile to a
    :class:`User` account.
    :type user: OneToOneField to :class:`User`
    :param favorite_city: A field for storing the user's favorite city.
    :type favorite_city: CharField, optional
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
