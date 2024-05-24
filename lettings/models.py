"""
Models for managing addresses and lettings in the application.

This module defines two models: :class:`lettings.Address` and :class:`lettings.Letting`. The Address model represents
a physical address with attributes such as number, street, city, state, zip code, and country ISO code.
The Letting model represents a letting (rental) property with a title and a one-to-one relationship with an Address.

Models:
    Address: Represents a physical address with various attributes.
    Letting: Represents a letting (rental) property with a title and an associated Address.

Attributes:
    Address:
        number (PositiveIntegerField): The street number of the address.
        street (CharField): The name of the street.
        city (CharField): The name of the city.
        state (CharField): The state abbreviation (e.g., 'CA' for California).
        zip_code (PositiveIntegerField): The ZIP code of the address.
        country_iso_code (CharField): The ISO code of the country (e.g., 'USA' for United States).

    Letting:
        title (CharField): The title or name of the letting property.
        address (OneToOneField): A one-to-one relationship with an Address.

Notes:
    - The Address model has a custom verbose name plural to display 'addresses' instead
      of 'addresss' in the admin interface.
    - Validators are used to enforce constraints on certain fields (e.g., MaxValueValidator
      for number and zip_code, MinLengthValidator for state and country_iso_code).

Usage:
    These models can be used to manage address information for letting properties.
    They can be accessed and manipulated through Django's ORM and are designed to be
    used in conjunction with Django's admin interface or custom views.

Example:
    To create a new letting property with an address::

        address = Address.objects.create(
            number=123,
            street='Main St',
            city='Exampleville',
            state='CA',
            zip_code=12345,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(title='Cozy Apartment', address=address)

:param MaxValueValidator: Imports MaxValueValidator from Django's core validators for model
field validation.
:param MinLengthValidator: Imports MinLengthValidator from Django's core validators for model
field validation.
:param models: Imports models module from Django's database package to define database models.
"""

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Model for managing physical addresses.

    Represents a physical address with attributes such as number, street, city, state,
    zip code, and country ISO code.

    Methods:
        __str__: Returns a string representation of the :class:`lettings.Address`.

    :param number: The street number of the :class:`lettings.Address`.
    :type number: PositiveIntegerField, required
    :param street: The name of the street.
    :type street: CharField, required
    :param city: The name of the city.
    :type city: CharField,required
    :param state: The state abbreviation (e.g., 'CA' for California).
    :type state: CharField, required
    :param zip_code: The ZIP code of the :class:`lettings.Address`.
    :type zip_code: PositiveIntegerField, required
    :param country_iso_code: The ISO code of the country (e.g., 'USA' for United States).
    :type country_iso_code: CharField, required
    """

    class Meta:
        verbose_name_plural = "addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Model for managing letting properties.

    Represents a :class:`lettings.Letting` (rental) property with a title and an associated :class:`lettings.Address`.

    Methods:
        __str__: Returns a string representation of the :class:`lettings.Letting` property.

    :param title: The title or name of the :class:`lettings.Letting` property.
    :type title: CharField, required
    :param address: A one-to-one relationship with an :class:`lettings.Address`.
    :type address: OneToOneField to :class:`lettings.Address`, required
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
