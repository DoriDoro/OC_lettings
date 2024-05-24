"""
Admin configuration for managing Lettings data.

This module registers the Lettings models (:class:`lettings.Address` and :class:`lettings.Letting`)
with the Django admin interface. This allows administrators to manage Lettings data directly
through the Django admin site.

Models Registered:
    - Address: Represents an address associated with a letting.
    - Letting: Represents a letting, including the address and title.

Note:
    By registering the models with the Django admin site using ``admin.site.register``,
    administrators gain access to the default admin interface for managing the
    registered models. Additional customization of the admin interface can be
    achieved by creating ModelAdmin subclasses and registering them instead.

:param admin: Django admin module for managing the administrative interface of a Django project.
"""

from django.contrib import admin

from lettings.models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)
