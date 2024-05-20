"""
Test cases for Profiles app views and models.

This module contains test cases for the views and models of the Profiles app
in a Django project. It includes tests for creating, updating, deleting profiles,
as well as views for rendering listing and detail views.

Attributes:
    get_user_model: A function provided by Django to get the currently active user model.
    UserModel: The user model used in the Django project.
    TestCase: A subclass of Django's TestCase class for writing unit tests.
    Http404: An exception raised when a requested object is not found.
    RequestFactory: A class provided by Django for creating mock request objects.
    reverse: A function provided by Django for generating URLs based on view names.

Classes:
    ProfileViewTestCase(TestCase): A subclass of TestCase to test the Profile model and views.
    ProfileIndexViewTestCase(TestCase): A subclass of TestCase to test the index view for profiles.
    ProfileDetailViewTestCase(ProfileViewTestCase): A subclass of TestCase to test the detail
    view for profiles.

Methods:
    setUpTestData: Method to set up test data before running tests.
    test_profile_index_view: Method to test the behavior of the index view for profiles.
    test_profile_id_view_successful: Method to test the behavior of the detail view for a valid
    profile username.
    test_profile_id_view_failed: Method to test the behavior of the detail view for an invalid
    profile username.

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
    Test case for Profile model and views.

    This class contains methods to test the behavior of Profile model and views.

    Attributes:
        USERNAME: A string representing the username for test user.
        USER_EMAIL: A string representing the email for test user.
        USER_PASSWORD: A string representing the password for test user.
        USER_FIRST_NAME: A string representing the first name for test user.
        USER_LAST_NAME: A string representing the last name for test user.

    Methods:
        setUpTestData: Method to set up test data before running tests.
    """

    USERNAME = "Test User"
    USER_EMAIL = "john.doe@mail.com"
    USER_PASSWORD = "TestPassword"
    USER_FIRST_NAME = "John"
    USER_LAST_NAME = "Doe"

    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(
            username=cls.USERNAME,
            password=cls.USER_PASSWORD,
            email=cls.USER_EMAIL,
            first_name=cls.USER_FIRST_NAME,
            last_name=cls.USER_LAST_NAME,
        )

        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Test City")


class ProfileIndexViewTestCase(TestCase):
    """
    Test case for the index view for profiles.

    This class contains a method to test the behavior of the index view for profiles.

    Methods:
        test_profile_index_view: Method to test the behavior of the index view for profiles.
    """

    def test_profile_index_view(self):
        request = RequestFactory().get(reverse("profiles:profiles_index"))
        response = index(request)

        self.assertEqual(response.status_code, 200)


class ProfileDetailViewTestCase(ProfileViewTestCase):
    """
    Test case for the detail view for profiles.

    This class contains methods to test the behavior of the detail view for profiles.

    Methods:
        test_profile_id_view_successful: Method to test the behavior of the detail view for
        a valid profile username.
        test_profile_id_view_failed: Method to test the behavior of the detail view for
        an invalid profile username.
    """

    def test_profile_id_view_successful(self):
        request = RequestFactory().get(
            reverse("profiles:profile", kwargs={"username": self.profile.user.username})
        )
        response = profile(request, username=self.profile.user.username)

        self.assertEqual(response.status_code, 200)

    def test_profile_id_view_failed(self):
        request = RequestFactory().get(
            reverse("profiles:profile", kwargs={"username": self.profile.user.username})
        )

        with self.assertRaises(Http404):
            profile(request, username="Invalid Test Username")
