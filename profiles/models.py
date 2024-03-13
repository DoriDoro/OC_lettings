"""
Model for managing user profiles in the application.

This module defines the Profile model, which represents user profiles in the application.
Each Profile is associated with a corresponding User model instance, establishing a one-to-one
relationship between users and their profiles.

Attributes:
    user (OneToOneField): A one-to-one relationship with the User model, linking each profile
                          to a user account.
    favorite_city (CharField): A field for storing the user's favorite city. This field is optional
                                and can be left blank.

Methods:
    __str__(): Returns a string representation of the profile, which is the username of the associated user.

Usage:
    The Profile model can be used to store additional information about users beyond what is provided
    by the built-in User model. This could include profile pictures, bio information, preferences,
    and more.

Example:
    To create a new user profile:
        user = User.objects.create(username='example_user', ...)
        profile = Profile.objects.create(user=user, favorite_city='New York')
"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Model for managing user profiles in the application.

    Represents user profiles in the application, associated with corresponding User model instances.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model, linking each profile
                              to a user account.
        favorite_city (CharField): A field for storing the user's favorite city. This field is optional
                                    and can be left blank.

    Methods:
        __str__(): Returns a string representation of the profile.

    Usage:
        The Profile model can be used to store additional information about users beyond what is provided
        by the built-in User model.

    Example:
        To create a new user profile:
            user = User.objects.create(username='example_user', ...)
            profile = Profile.objects.create(user=user, favorite_city='New York')
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
