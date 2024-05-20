"""
Test cases for Lettings app views and models.

This module contains test cases for the views and models of the Lettings app
in a Django project. It includes tests for creating, updating, deleting lettings
and addresses, as well as views for rendering listing and detail views.

Attributes:
    TestCase: A subclass of Django's TestCase class for writing unit tests.
    Http404: An exception raised when a requested object is not found.
    RequestFactory: A class provided by Django for creating mock request objects.
    reverse: A function provided by Django for generating URLs based on view names.

Classes:
    LettingViewTestCase(TestCase): A subclass of TestCase to test the Letting model and views.
    LettingsIndexViewTestCase(TestCase): A subclass of TestCase to test the index view for
    lettings.
    LettingsDetailViewTestCase(LettingViewTestCase): A subclass of TestCase to test the detail
    view for lettings.

Methods:
    setUpTestData: Method to set up test data before running tests.
    test_letting_index_view: Method to test the behavior of the index view for lettings.
    test_letting_id_view_successful: Method to test the behavior of the detail view for a
    valid letting ID.
    test_letting_id_view_failed: Method to test the behavior of the detail view for an
    invalid letting ID.

"""

from django.http import Http404
from django.test import TestCase, RequestFactory
from django.urls import reverse

from lettings.models import Letting, Address
from lettings.views import index, letting


class LettingViewTestCase(TestCase):
    """
    Test case for Letting model and views.

    This class contains methods to test the behavior of Letting model and views.

    Attributes:
        address: An instance of the Address model.
        letting: An instance of the Letting model.

    Methods:
        setUpTestData: Method to set up test data before running tests.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the Address model.
        """

        cls.address = Address.objects.create(
            number=18,
            street="Test Street View",
            city="Test City View",
            state="Test State View",
            zip_code=52369,
            country_iso_code=74125,
        )

        cls.letting = Letting.objects.create(title="Test House 1", address=cls.address)


class LettingsIndexViewTestCase(TestCase):
    """
    Test case for the index view for lettings.

    This class contains a method to test the behavior of the index view for lettings.

    Methods:
        test_letting_index_view: Method to test the behavior of the index view for lettings.
    """

    def test_letting_index_view(self):
        """
        Method to test the behavior of the index view for lettings.
        """
        request = RequestFactory().get(reverse("lettings:lettings_index"))
        response = index(request)

        self.assertEqual(response.status_code, 200)


class LettingsDetailViewTestCase(LettingViewTestCase):
    """
    Test case for the detail view for lettings.

    This class contains methods to test the behavior of the detail view for lettings.

    Methods:
        test_letting_id_view_successful: Method to test the behavior of the detail view for
            a valid letting ID.
        test_letting_id_view_failed: Method to test the behavior of the detail view for
            an invalid letting ID.
    """

    def test_letting_id_view_successful(self):
        """
        Method to test the behavior of the detail view for a valid letting ID.
        """

        request = RequestFactory().get(
            reverse("lettings:letting", kwargs={"letting_id": self.letting.id})
        )
        response = letting(request, letting_id=self.letting.id)

        self.assertEqual(response.status_code, 200)

    def test_letting_id_view_failed(self):
        """
        Method to test the behavior of the detail view for  an invalid letting ID.
        """

        request = RequestFactory().get(
            reverse("lettings:letting", kwargs={"letting_id": self.letting.id})
        )
        with self.assertRaises(Http404):
            letting(request, letting_id=6)
