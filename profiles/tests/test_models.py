"""
Test module for profiles app models.

This module contains test cases for the models of the Profiles app in a Django project.
It includes tests for creating, updating, and deleting user profiles.

Attributes:
    get_user_model: A function provided by Django to get the currently active user model.
    TestCase: A subclass of Django's TestCase class for writing unit tests.
    IntegrityError: An exception raised when a database integrity constraint is violated.
    ValueError: An exception is often raised in Python when an invalid value is assigned to a
    variable or passed to a function while calling it.

Classes:
    ModelTestCase: A base test case for model testing.
    UserTestCase: A test case for the user model.
    ProfileTestCase: A test case for the profile model.

Methods:
    ModelTestCase.setUpTestData: Method to set up test data before running tests.
    UserTestCase.test_user_creation_successful: Method to test successful user creation.
    UserTestCase.test_user_creation_failed: Method to test user creation with invalid data.
    UserTestCase.test_user_creation_second_time: Method to test user creation when the user already exists.
    UserTestCase.test_user_delete_successful: Method to test successful user deletion.
    ProfileTestCase.setUp: Method to set up test data for the Profile model.
    ProfileTestCase.test_profile_creation_successful: Method to test successful profile creation.
    ProfileTestCase.test_profile_delete_successful: Method to test successful profile deletion.
    ProfileTestCase.test_profile_str: Method to test string representation of the profile.

:param get_user_model: A function provided by Django to get the currently active user model.
:param TestCase: A subclass of Django's TestCase class for writing unit tests.
:param IntegrityError: An exception raised when a database integrity constraint is violated.
:param ValueError: An exception is often raised in Python when an invalid value is assigned to a
    variable or passed to a function while calling it.

:return: No return value.
:rtype: None
"""

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

from profiles.models import Profile

UserModel = get_user_model()


class ModelTestCase(TestCase):
    """
    Base test case class for model testing.

    Attributes:
        USERNAME (str): Username for test user.
        USER_EMAIL (str): Email address for test user.
        USER_PASSWORD (str): Password for test user.
        USER_FIRST_NAME (str): First name for test user.
        USER_LAST_NAME (str): Last name for test user.

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
        """
        Set up test data for the user model.

        Creates a user instance with predefined test data.
        """

        cls.user = UserModel.objects.create_user(
            username=cls.USERNAME,
            password=cls.USER_PASSWORD,
            email=cls.USER_EMAIL,
            first_name=cls.USER_FIRST_NAME,
            last_name=cls.USER_LAST_NAME,
        )


class UserTestCase(ModelTestCase):
    """
    Test case class for the user model.

    Attributes:
        TEST_USERNAME (str): Test username for new user.
        TEST_EMAIL (str): Test email address for new user.
        TEST_FIRST_NAME (str): Test first name for new user.
        TEST_LAST_NAME (str): Test last name for new user.
    """

    TEST_USERNAME = "Test Profile User"
    TEST_EMAIL = "jane.doe@mail.com"
    TEST_FIRST_NAME = "Jane"
    TEST_LAST_NAME = "Doe"

    def test_user_creation_successful(self):
        """
        Test successful creation of a user instance.

        Asserts that the created user instance has the expected attributes.
        """

        user = UserModel.objects.create_user(
            username=self.TEST_USERNAME,
            password=self.USER_PASSWORD,
            email=self.TEST_EMAIL,
            first_name=self.TEST_FIRST_NAME,
            last_name=self.TEST_LAST_NAME,
        )
        self.assertEqual(user.username, self.TEST_USERNAME)
        self.assertEqual(user.email, self.TEST_EMAIL)
        self.assertEqual(user.first_name, self.TEST_FIRST_NAME)
        self.assertEqual(user.last_name, self.TEST_LAST_NAME)

    def test_user_creation_failed(self):
        """
        Test failed creation of a user instance.

        This method tests the scenario where a user instance creation fails due to invalid data.

        :raises ValueError: If invalid data is used for user creation.
        """

        invalid_data = [
            {"username": "", "email": "", "password": None},
            {"username": "", "email": None, "password": ""},
            {"username": "", "email": "testuser1@mail.com", "password": ""},
            {"username": "", "email": "testuser2@mail.com", "password": None},
            {"username": "", "email": "", "password": self.USER_PASSWORD},
            {"username": "", "email": None, "password": self.USER_PASSWORD},
        ]

        for data in invalid_data:
            with self.assertRaises(ValueError):
                UserModel.objects.create_user(**data)

    def test_user_creation_second_time(self):
        """
        Test failed creation of a user instance when the user already exists.

        This method tests the scenario where a user instance creation fails due to an attempt to create
        a user with the same username.

        :raises IntegrityError: If attempting to create a user with the same username.
        """

        with self.assertRaises(IntegrityError):
            UserModel.objects.create_user(
                username=self.USERNAME,
                password=self.USER_PASSWORD,
                email=self.USER_EMAIL,
                first_name=self.USER_FIRST_NAME,
                last_name=self.USER_LAST_NAME,
            )

    def test_user_delete_successful(self):
        """
        Test successful deletion of a user instance.

        Asserts that the user instance is deleted from the database.
        """

        self.assertTrue(UserModel.objects.filter(username=self.user.username).exists())
        self.user.delete()
        self.assertFalse(UserModel.objects.filter(username=self.user.username).exists())


class ProfileTestCase(ModelTestCase):
    """
    Test case class for testing the Profile model.

    Attributes:
        FAVORITE_CITY (str): Test favorite city for the profile.
    """

    FAVORITE_CITY = "Rennes"

    def setUp(self):
        """
        Set up test data for the Profile model.

        Creates a Profile instance with the predefined test data.
        """

        super().setUp()
        self.profile = Profile.objects.create(
            user=self.user, favorite_city=self.FAVORITE_CITY
        )

    def test_profile_creation_successful(self):
        """
        Test successful creation of a Profile instance.

        Asserts that the created Profile instance has the expected attributes.
        """

        self.assertEqual(self.profile.user.username, self.USERNAME)
        self.assertEqual(self.profile.user.email, self.USER_EMAIL)
        self.assertEqual(self.profile.favorite_city, self.FAVORITE_CITY)

    def test_profile_delete_successful(self):
        """
        Test successful deletion of a Profile instance.

        Asserts that the Profile instance is deleted from the database.
        """

        self.assertTrue(Profile.objects.filter(user=self.user).exists())
        self.profile.delete()
        self.assertFalse(Profile.objects.filter(user=self.user).exists())

    def test_profile_str(self):
        """
        Test the string representation of a Profile instance.

        Asserts that the string representation is as expected.
        """

        self.assertEqual(str(self.profile), self.USERNAME)
