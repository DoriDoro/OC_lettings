"""
Views for managing user profiles in the profiles app.

This module defines views for handling HTTP requests related to :class:`profiles.Profile` in the
profiles app of the project.

Views defined here include:
    - index: Renders the profiles index page, displaying a list of all :class:`profiles.Profile`.
    - profile: Renders the details page for a specific :class:`profiles.Profile` identified by
      username.

Usage:
    These views can be used to display information about :class:`profiles.Profile`, including
    their usernames, favorite cities, or any other profile-related data. They interact
    with the :class:`profiles.Profile` model to retrieve data from the database and render it in
    the appropriate templates.

Example:
    To render the profiles index page:
        Profile.objects.all()  # Retrieve all user profiles from the database.
        render(request, 'profiles_index.html', context)  # Render the index page with the profile
        data.

    To render the details page for a specific user profile:
        get_object_or_404(Profile, user__username=username)  # Retrieve the profile with the
        specified username.
        render(request, 'profile.html', context)  # Render the details page with the profile data.

:param Letting: Represents a :class:`lettings.Letting` (rental) property in the database.
:type Letting: class:`lettings.Letting`
:param render: A module to render templates in Django views.
:param get_object_or_404: A function provided by Django that retrieves an object from the database
    or raises a Http404 exception if the object does not exist.
"""

from django.shortcuts import render, get_object_or_404

from profiles.models import Profile


def index(request):
    """
    Render the profiles index page.

    This view retrieves all user profiles from the database and renders
    the profiles index page ('profiles_index.html') with a list of user profiles.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """
    Render the details page for a specific user profile.

    This view retrieves a user profile with the specified username from the database
    and renders the details page ('profile.html') with information about the user profile.

    Parameters:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user profile to display.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """

    single_profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": single_profile}
    return render(request, "profile.html", context)
