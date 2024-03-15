"""
Admin configuration for managing Lettings data.

This module registers the Lettings models (Address and Letting) with the Django
admin interface. This allows administrators to manage Lettings data directly
through the Django admin site.

Models Registered:
    - Address: Allows administrators to view, create, edit, and delete address
               records associated with lettings.
    - Letting: Allows administrators to view, create, edit, and delete letting
               records, which represent rental properties.

Note:
    By registering the models with the Django admin site using 'admin.site.register',
    administrators gain access to the default admin interface for managing the
    registered models. Additional customization of the admin interface can be
    achieved by creating ModelAdmin subclasses and registering them instead.
"""

from django.contrib import admin

from lettings.models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)
