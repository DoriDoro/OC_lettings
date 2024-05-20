"""
Views for managing user profiles in the profiles app.

This module defines views for handling HTTP requests related to user profiles
in the profiles app of the project.

Views defined here include:
    - index: Renders the profiles index page, displaying a list of all user profiles.
    - profile: Renders the details page for a specific user profile identified by username.

Attributes:
    Profile:
        Represents user profiles in the application.

Methods:
    index: Renders the profiles index page with a list of all user profiles.
    profile: Renders the details page for a specific user profile.

Usage:
    These views can be used to display information about user profiles, including
    their usernames, favorite cities, or any other profile-related data. They interact
    with the Profile model to retrieve data from the database and render it in the
    appropriate templates.

Example:
    To render the profiles index page:
        Profile.objects.all()  # Retrieve all user profiles from the database.
        render(request, 'profiles_index.html', context)  # Render the index page with the profile
        data.

    To render the details page for a specific user profile:
        get_object_or_404(Profile, user__username=username)  # Retrieve the profile with the
        specified username.
        render(request, 'profile.html', context)  # Render the details page with the profile data.
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
