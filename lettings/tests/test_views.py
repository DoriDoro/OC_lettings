"""
Test cases for Lettings app views and models.

This module contains test cases for the views and models of the Lettings app in a Django project.
It includes tests for creating, updating, deleting :class:`lettings.Letting` and
:class:`lettings.Address`, as well as views for rendering listing and detail views.

Classes:
    - LettingViewTestCase (TestCase): A subclass of TestCase to test the :class:`lettings.Letting`
      model and views.
    - LettingsIndexViewTestCase (LettingViewTestCase): A subclass of LettingViewTestCase to test
      the index view for :class:`lettings.Letting`.
    - LettingsDetailViewTestCase (LettingViewTestCase): A subclass of LettingViewTestCase to test
      the detail view for :class:`lettings.Letting`.

Methods:
    - LettingViewTestCase.setUpTestData: Method to set up test data before running tests.
    - LettingsIndexViewTestCase.test_letting_index_view: Method to test the behavior of the index
      view for :class:`lettings.Letting`.
    - LettingsDetailViewTestCase.test_letting_id_view_successful: Method to test the behavior of
      the detail view for a valid :class:`lettings.Letting` ID.
    - LettingsDetailViewTestCase.test_letting_id_view_failed: Method to test the behavior of the
      detail view for an invalid :class:`lettings.Letting` ID.

:param Http404: An exception raised when a requested object is not found.
:param TestCase: A subclass of Django's TestCase class for writing unit tests.
:param RequestFactory: A class provided by Django for creating mock request objects.
:param reverse: A function provided by Django for generating URLs based on view names.
"""

from django.http import Http404
from django.test import TestCase, RequestFactory
from django.urls import reverse

from lettings.models import Letting, Address
from lettings.views import index, letting


class LettingViewTestCase(TestCase):
    """
    Base test case for :class:`lettings.Letting` model and views.

    :param address: An instance of the :class:`lettings.Address`.
    :type address: class:`lettings.Address`
    :param letting: An instance of the :class:`lettings.Letting`.
    :type letting: class:`lettings.Letting`
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the LettingViewTestCase class.

        Creates an :class:`lettings.Address` instance and a :class:`lettings.Letting` instance for
        testing purposes.

        :param number: An attribute of an instance of :class:`lettings.Address`.
        :type number: int, required
        :param street: An attribute of an instance of :class:`lettings.Address`.
        :type street: str, required
        :param city: An attribute of an instance of :class:`lettings.Address`.
        :type city: str, required
        :param state: An attribute of an instance of :class:`lettings.Address`.
        :type state: str, required
        :param zip_code: An attribute of an instance of :class:`lettings.Address`.
        :type zip_code: int, required
        :param country_iso_code: An attribute of an instance of :class:`lettings.Address`.
        :type country_iso_code: int, required
        :param title: An attribute of an instance of :class:`lettings.Address`.
        :type title: str, required
        :param address: An instance of :class:`lettings.Address`.
        :type address: class: `lettings.Address`
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


class LettingsIndexViewTestCase(LettingViewTestCase):
    """
    Test case for the index view for :class:`lettings.Letting`.

    This class contains a method to test the behavior of the index view for
    :class:`lettings.Letting` and inherit from LettingViewTestCase.

    Methods:
        - test_letting_index_view: Method to test :class:`lettings.Letting` index view.
    """

    def test_letting_index_view(self):
        """
        Test the behavior of the index view for :class:`lettings.Letting`.

        Simulates a GET request to the index view and asserts that the response status code is 200.

        :return: None
        :rtype: None
        """
        request = RequestFactory().get(reverse("lettings:lettings_index"))
        response = index(request)

        self.assertEqual(response.status_code, 200)


class LettingsDetailViewTestCase(LettingViewTestCase):
    """
    Test case for the detail view for :class:`lettings.Letting`.

    This class contains methods to test the behavior of the detail view for
    :class:`lettings.Letting` and inherit from LettingViewTestCase.

    Methods:
        - test_letting_id_view_successful: Method tests the successful detail view of one
          :class:`lettings.Letting`.
        - test_letting_id_view_failed: Method tests the failure of one :class:`lettings.Letting`
          detail view.
    """

    def test_letting_id_view_successful(self):
        """
        Test the behavior of the detail view for a valid :class:`lettings.Letting` ID.

        Simulates a GET request to the detail view with a valid :class:`lettings.Letting` ID and
        asserts that the response status code is 200.

        :return: None
        :rtype: None
        """

        request = RequestFactory().get(
            reverse("lettings:letting", kwargs={"letting_id": self.letting.id})
        )
        response = letting(request, letting_id=self.letting.id)

        self.assertEqual(response.status_code, 200)

    def test_letting_id_view_failed(self):
        """
        Test the behavior of the detail view for an invalid :class:`lettings.Letting` ID.

        Simulates a GET request to the detail view with an invalid :class:`lettings.Letting` ID and
        asserts that a Http404 exception is raised.

        :raises Http404: If the :class:`lettings.Letting` ID does not exist.
        """

        request = RequestFactory().get(
            reverse("lettings:letting", kwargs={"letting_id": self.letting.id})
        )
        with self.assertRaises(Http404):
            letting(request, letting_id=6)
