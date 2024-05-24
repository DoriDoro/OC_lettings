"""
Test cases for Profiles app views and models.

This module contains test cases for the views and models of the Profiles app
in a Django project. It includes tests for creating, updating, deleting profiles,
as well as views for rendering listing and detail views.

Classes:
    - ProfileViewTestCase(TestCase): A subclass of TestCase to test the Profile model and views.
    - ProfileIndexViewTestCase(ProfileViewTestCase): A subclass of TestCase to test the index view
      for profiles.
    - ProfileDetailViewTestCase(ProfileViewTestCase): A subclass of TestCase to test the detail
      view for profiles.

Methods:
    - ProfileViewTestCase.setUpTestData: Method to set up test data before running tests.
    - ProfileIndexViewTestCase.test_profile_index_view: Method to test the behavior of the index
      view for profiles.
    - ProfileDetailViewTestCase.test_profile_id_view_successful: Method to test the behavior of the
      detail view for a valid profile username.
    - ProfileDetailViewTestCase.test_profile_id_view_failed: Method to test the behavior of the
      detail view for an invalid profile username.

:param get_user_model: A function provided by Django to get the currently active user model.
:param Http404: An exception raised when a requested object is not found.
:param TestCase: A subclass of Django's TestCase class for writing unit tests.
:param RequestFactory: A class provided by Django for creating mock request objects.
:param reverse: A function provided by Django for generating URLs based on view names.
"""

from django.contrib.auth import get_user_model
from django.http import Http404
from django.test import TestCase, RequestFactory
from django.urls import reverse

from profiles.models import Profile
from profiles.views import index, profile

UserModel = get_user_model()


class ProfileViewTestCase(TestCase):
    """
    Base test case for class:`profile.Profile` model and views.

    This class contains methods to test the behavior of class:`profile.Profile` model and views.

    Methods:
        - setUpTestData: Method to set up test data before running tests.

    :param USERNAME: A string representing the username for test user.
    :type USERNAME: str, required
    :param USER_EMAIL: A string representing the email for test user.
    :type USER_EMAIL: str, required
    :param USER_PASSWORD: A string representing the password for test user.
    :type USER_PASSWORD: str, required
    :param USER_FIRST_NAME: A string representing the first name for test user.
    :type USER_FIRST_NAME: str, required
    :param USER_LAST_NAME: A string representing the last name for test user.
    :type USER_LAST_NAME: str
    :param user: An instance of :class:`User` model.
    :type user: class:`User`
    :param profile: An instance of :class:`profile.Profile` model.
    :type profile: class:`profile.Profile`
    """

    USERNAME = "Test User"
    USER_EMAIL = "john.doe@mail.com"
    USER_PASSWORD = "TestPassword"
    USER_FIRST_NAME = "John"
    USER_LAST_NAME = "Doe"

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the :class:`User` model.

        Creates a :class:`User` and a :class:`profile.Profile` instance with predefined test data.

        :param username: An attribute of an instance of :class:`User` model.
        :type username: str, required
        :param password: An attribute of an instance of :class:`User` model.
        :type password: str, required
        :param email: An attribute of an instance of :class:`User` model.
        :type email: str, required
        :param first_name: An attribute of an instance of :class:`User` model.
        :type first_name: str, required
        :param last_name: An attribute of an instance of :class:`User` model.
        :type last_name: str, required
        :param user: An instance of a :class:`User` model.
        :type user: class:`User`
        :param favorite_city: An attribute of an instance of :class:`profile.Profile` model.
        :type favorite_city: str, optional
        """

        cls.user = UserModel.objects.create_user(
            username=cls.USERNAME,
            password=cls.USER_PASSWORD,
            email=cls.USER_EMAIL,
            first_name=cls.USER_FIRST_NAME,
            last_name=cls.USER_LAST_NAME,
        )

        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Test City")


class ProfileIndexViewTestCase(ProfileViewTestCase):
    """
    Test case for the index view for profiles.

    This class contains a method to test the behavior of the index view for profiles.

    Methods:
        - test_profile_index_view: Method to test the behavior of the index view for profiles.
    """

    def test_profile_index_view(self):
        """
        Test the behavior of the index view for profiles.

        This function creates a mock HTTP GET request to the index view for profiles
        and checks if the response status code is 200, indicating a successful request.

        :return: None
        :rtype: None
        """

        request = RequestFactory().get(reverse("profiles:profiles_index"))
        response = index(request)

        self.assertEqual(response.status_code, 200)


class ProfileDetailViewTestCase(ProfileViewTestCase):
    """
    Test case for the detail view for profiles.

    This class contains methods to test the behavior of the detail view for profiles.

    Methods:
        - test_profile_id_view_successful: Method to test the behavior of the detail view for a
          valid profile username.
        - test_profile_id_view_failed: Method to test the behavior of the detail view for an
          invalid profile username.
    """

    def test_profile_id_view_successful(self):
        """
        Test the behavior of the detail view for a valid profile username.

        This function creates a mock HTTP GET request to the detail view for a valid
        profile username and checks if the response status code is 200, indicating
        a successful request.

        :return: None
        :rtype: None
        """

        request = RequestFactory().get(
            reverse("profiles:profile", kwargs={"username": self.profile.user.username})
        )
        response = profile(request, username=self.profile.user.username)

        self.assertEqual(response.status_code, 200)

    def test_profile_id_view_failed(self):
        """
        Test the behavior of the detail view for an invalid profile username.

        This function creates a mock HTTP GET request to the detail view for an invalid
        profile username and checks if the view raises an Http404 exception, indicating
        that the requested object was not found.

        :raises Http404: When attempting to access a profile with an invalid username.
        """

        request = RequestFactory().get(
            reverse("profiles:profile", kwargs={"username": self.profile.user.username})
        )

        with self.assertRaises(Http404):
            profile(request, username="Invalid Test Username")
