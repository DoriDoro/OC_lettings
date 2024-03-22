"""
Test case for the index view in the core app.

This module contains a TestCase subclass which tests the behavior of the index view
defined in the core app's views module. The index view is responsible for rendering
the homepage of the application.

Attributes:
    TestCase: A subclass of Django's TestCase class for writing unit tests.
    RequestFactory: A class provided by Django for creating mock request objects.
    reverse: A function provided by Django for generating URLs based on view names.

Classes:
    CoreViewTestCase(TestCase): A subclass of TestCase to test the index view.

Methods:
    test_core_index_view: Method to test the behavior of the index view.
"""

from django.test import TestCase, RequestFactory
from django.urls import reverse

from core.views import index, trigger_error


class CoreViewTestCase(TestCase):
    """
    Test case for the CoreViewTestCase class.

    This class contains test methods to verify the behavior of the index view in the core app.

    Parameter:
        TestCase: A subclass of Django's TestCase class for writing unit tests.

    Methods:
        test_core_index_view: Method to test the behavior of the index view.
    """

    def test_core_index_view(self):
        """
        Test the behavior of the index view in the core app.

        This method tests the behavior of the index view by simulating a GET request
        to the index view URL using Django's RequestFactory. It then calls the index
        view function and asserts that the response status code is 200, indicating
        a successful response.

        Returns:
            None

        Raises:
            AssertionError: If the response status code is not 200.

        """

        request = RequestFactory().get(reverse('core:index'))
        response = index(request)

        self.assertEqual(response.status_code, 200)

    def test_core_trigger_error_view(self):
        request = RequestFactory().get(reverse('core:trigger_error_sentry'))
        with self.assertRaises(ZeroDivisionError):
            trigger_error(request)
