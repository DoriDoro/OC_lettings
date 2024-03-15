"""
URL Configuration for the profiles app.

This module defines URL patterns for the profiles app of the project. The profiles
app is responsible for managing user profiles and related views.

Patterns defined here include:
    - /profiles/ - URL pattern for the profiles index page, displaying a list of all user profiles.
    - /profiles/<str:username>/ - URL pattern for viewing details of a specific user profile
        identified by the username.

Notes:
    - The URL patterns are namespaced under 'profiles' to prevent naming conflicts and provide
        better organization and readability.
    - Views for handling these URL patterns are defined in the 'views.py' module of
        the profiles app.

Usage:
    This file serves as the URL configuration for the profiles app. It includes URL patterns for
    various parts of the profiles functionality, such as listing all user profiles and viewing
    individual user profiles.
"""

from django.urls import path

from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('profiles/', views.index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]
