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
    CoreViewTestCase: A subclass of TestCase to test the index view.

:param TestCase: A subclass of Django's TestCase class for writing unit tests.
:param RequestFactory: A class provided by Django for creating mock request objects.
:param reverse: A function provided by Django for generating URLs based on view names.
"""

from django.test import TestCase, RequestFactory
from django.urls import reverse

from core.views import index, trigger_error


class CoreViewTestCase(TestCase):
    """
    Test case for the CoreViewTestCase class.

    This class contains test methods to verify the behavior of the index view in the core app.

    Methods:
        test_core_index_view: Method to test the behavior of the index view.
        test_core_trigger_error_view: Method to test the behavior of the trigger_error view.
    """

    def test_core_index_view(self):
        """
        Test the behavior of the index view in the core app.

        This method tests the behavior of the index view by simulating a GET request
        to the index view URL using Django's RequestFactory. It then calls the index
        view function and asserts that the response status code is 200, indicating
        a successful response.

        :return: None
        :rtype: None
        :raises AssertionError: If the response status code is not 200.
        """

        request = RequestFactory().get(reverse('core:index'))
        response = index(request)

        self.assertEqual(response.status_code, 200)

    def test_core_trigger_error_view(self):
        """
        Test the behavior of the trigger_error view in the core app.

        This method tests the trigger_error view by simulating a GET request
        to the trigger_error view URL using Django's RequestFactory. It asserts
        that a ZeroDivisionError is raised when the view is called.

        :return: None
        :rtype: None
        :raises ZeroDivisionError: Always, since the view triggers this error.
        """

        request = RequestFactory().get(reverse('core:trigger_error_sentry'))
        with self.assertRaises(ZeroDivisionError):
            trigger_error(request)
