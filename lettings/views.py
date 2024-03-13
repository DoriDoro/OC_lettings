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

from lettings.models import Letting


def index(request):
    """
    Render the lettings index page.

    This view retrieves all letting properties from the database and renders
    the lettings index page ('lettings_index.html') with a list of letting properties.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    Render the details page for a specific letting property.

    This view retrieves a letting property with the specified ID from the database
    and renders the details page ('letting.html') with information about the letting property,
    including its title and address.

    Parameters:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting property to display.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """

    single_letting = get_object_or_404(Letting, pk=letting_id)
    context = {
        'title': single_letting.title,
        'address': single_letting.address,
    }
    return render(request, 'letting.html', context)
