"""
Views for handling letting properties in the lettings app.

This module defines views for handling HTTP requests related to letting properties
in the lettings app of the project.

Views defined here include:
    - index: Renders the lettings index page, displaying a list of all letting properties.
    - letting: Renders the details page for a specific letting property identified by its ID.

Attributes:
    Letting:
        Represents a letting (rental) property in the database.

Methods:
    index: Renders the lettings index page with a list of all letting properties.
    letting: Renders the details page for a specific letting property.

Usage:
    These views can be used to display information about letting properties, including
    their titles and addresses. They interact with the Letting model to retrieve data
    from the database and render it in the appropriate templates.

Example:
    To render the lettings index page:
        Letting.objects.all()
            # Retrieve all letting properties from the database.
        render(request, 'lettings_index.html', context)
            # Render the index page with the lettings data.

    To render the details page for a specific letting property:
        get_object_or_404(Letting, pk=letting_id)
            # Retrieve the letting property with the specified ID.
        render(request, 'letting.html', context)
            # Render the details page with the letting data.
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from lettings.models import Letting


class LettingListView(ListView):
    model = Letting
    template_name = 'lettings_index.html'
    context_object_name = 'lettings_list'


class LettingDetailView(DetailView):
    model = Letting
    template_name = 'letting.html'

    def get_object(self, queryset=None):
        letting_id = self.kwargs.get('letting_id')
        return get_object_or_404(Letting, pk=letting_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['address'] = self.object.address
        return context
