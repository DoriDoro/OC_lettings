"""
URL Configuration for the project.

This module defines the top-level URL patterns for the project. It includes URL patterns
for the Django admin interface and includes URL patterns from various apps within the project.

Patterns defined here include:
    - /admin/ - URL pattern for accessing the Django admin interface.
    - / - URL patterns included from the 'core', 'lettings', and 'profiles' apps.

Notes:
    The URL patterns for individual apps are included using the 'include' function, allowing for
    modular and organized URL configuration. Each app's URL patterns are namespaced to prevent
    naming conflicts and provide better organization and readability.

:param admin: The Django admin site instance.
:param path: The function used for defining URL patterns.
:param include: The function used for including URL patterns from other apps.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("", include("lettings.urls", namespace="lettings")),
    path("", include("profiles.urls", namespace="profiles")),
]
