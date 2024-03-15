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
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from profiles.models import Profile


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles_index.html'
    # overwrites, otherwise: templates/app_name/profile_list.html
    context_object_name = 'profiles_list'  # renames the context_name, otherwise: profile_list


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(Profile, user__username=username)
