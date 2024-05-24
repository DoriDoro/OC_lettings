"""
Test module for profiles app models.

This module contains test cases for the models of the Profiles app in a Django project.
It includes tests for creating, updating, and deleting user profiles.

Attributes:
    get_user_model (Function): A function provided by Django to get the currently active user model.
    IntegrityError (Exception): An exception raised when a database integrity constraint is violated.
    TestCase (TestCase): A subclass of Django's TestCase class for writing unit tests.
    ValueError (Exception): An exception is often raised in Python when an invalid value is assigned to a
    variable or passed to a function while calling it.

Classes:
    ModelTestCase (TestCase): A base test case for model testing.
    UserTestCase (ModelTestCase): A test case for the user model.
    ProfileTestCase (ModelTestCase): A test case for the profile model.

Methods:
    ModelTestCase.setUpTestData: Method to set up test data before running tests.
    UserTestCase.test_user_creation_successful: Method to test successful :class:`User` creation.
    UserTestCase.test_user_creation_failed: Method to test :class:`User` creation with invalid data.
    UserTestCase.test_user_creation_second_time: Method to test :class:`User` creation when the user already exists.
    UserTestCase.test_user_delete_successful: Method to test successful :class:`User` deletion.
    ProfileTestCase.setUp: Method to set up test data for the :class:`profile.Profile` model.
    ProfileTestCase.test_profile_creation_successful: Method to test successful :class:`profile.Profile` creation.
    ProfileTestCase.test_profile_delete_successful: Method to test successful :class:`profile.Profile` deletion.
    ProfileTestCase.test_profile_str: Method to test string representation of the :class:`profile.Profile`.

:param get_user_model: A function provided by Django to get the currently active :class:`User` model.
:param TestCase: A subclass of Django's TestCase class for writing unit tests.
:param IntegrityError: An exception raised when a database integrity constraint is violated.
:param ValueError: An exception is often raised in Python when an invalid value is assigned to a
    variable or passed to a function while calling it.
"""

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

from profiles.models import Profile

UserModel = get_user_model()


class ModelTestCase(TestCase):
    """
    Base test case class for model testing.

    Methods:
        setUpTestData: Method to set up test data before running tests.

    :param USERNAME: Username for test :class:`User`.
    :type USERNAME: str, required
    :param USER_EMAIL: Email address for test :class:`User`.
    :type USER_EMAIL: str, required
    :param USER_PASSWORD: Password for test :class:`User`.
    :type USER_PASSWORD: str, required
    :param USER_FIRST_NAME: First name for test :class:`User`.
    :type USER_FIRST_NAME: str, required
    :param USER_LAST_NAME: Last name for test :class:`User`.
    :type USER_LAST_NAME: str, required
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

        Creates a :class:`User` instance with predefined test data.

        :param username: An attribute of an instance of :class:`User` model.
        :type username: str, reuqired
        :param password: An attribute of an instance of :class:`User` model.
        :type password: str, required
        :param email: An attribute of an instance of :class:`User` model.
        :type email: str, required
        :param first_name: An attribute of an instance of :class:`User` model.
        :type first_name: str, required
        :param last_name: An attribute of an instance of :class:`User` model.
        :type last_name: str, required
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
    Test case class for the :class:`User` model which inherits from ModelTestCase.

    Methods:
        test_user_creation_successful: Method to test the successful creation of a :class:`User` instance.
        test_user_creation_failed: Method to test a failure of creation of a :class:`User` instance.
        test_user_creation_second_time: Method to test creation of :class:`User` instance a second time.
        test_user_delete_successful: Method to test the deletion of a :class:`User` instance.

    :param TEST_USERNAME: Test username for new :class:`User`.
    :type TEST_USERNAME: str, required
    :param TEST_EMAIL: Test email address for new :class:`User`.
    :type TEST_EMAIL: str, required
    :param TEST_FIRST_NAME: Test first name for new :class:`User`.
    :type TEST_FIRST_NAME: str, required
    :param TEST_LAST_NAME: Test last name for new :class:`User`.
    :type TEST_LAST_NAME: str, required
    """

    TEST_USERNAME = "Test Profile User"
    TEST_EMAIL = "jane.doe@mail.com"
    TEST_FIRST_NAME = "Jane"
    TEST_LAST_NAME = "Doe"

    def test_user_creation_successful(self):
        """
        Test successful creation of a :class:`User` instance.

        Asserts that the created :class:`User` instance has the expected attributes.

        :return: None
        :rtype: None
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
        Test failed creation of a :class:`User` instance.

        This method tests the scenario where a user instance creation fails due to invalid data.

        :raises ValueError: If invalid data is used for :class:`User` creation.
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
        Test failed creation of a :class:`User` instance when the user already exists.

        This method tests the scenario where a :class:`User` instance creation fails due to an attempt to create
        a user with the same username.

        :raises IntegrityError: If attempting to create a :class:`User` with the same username.
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
        Test successful deletion of a :class:`User` instance.

        Asserts that the :class:`User` instance is deleted from the database.

        :return: None
        :rtype: None
        """

        self.assertTrue(UserModel.objects.filter(username=self.user.username).exists())
        self.user.delete()
        self.assertFalse(UserModel.objects.filter(username=self.user.username).exists())


class ProfileTestCase(ModelTestCase):
    """
    Test case class for testing the :class:`profile.Profile` model which inherits from ModelTestCase.

    Methods:
        setUp: Method to set up test data before running tests.
        test_profile_creation_successful: Method to successfully create a :class:`profile.Profile` instance.
        test_profile_delete_successful: Method to test the deletion of a :class:`profile.Profile` instance.
        test_profile_str: Method to test the string representative of the :class:`profile.Profile` instance.

    :param FAVORITE_CITY: Test favorite city for the profile.
    :type FAVORITE_CITY: str, required
    """

    FAVORITE_CITY = "Rennes"

    def setUp(self):
        """
        Set up test data for the :class:`profile.Profile` model.

        Creates a :class:`profile.Profile` instance with the predefined test data.

        :param user: An attribute of an instance of :class:`User`.
        :type user: class:`User` instance
        :param favorite_city: An attribute of an instance of :class:`User`.
        :type favorite_city: str, required
        """

        super().setUp()
        self.profile = Profile.objects.create(
            user=self.user, favorite_city=self.FAVORITE_CITY
        )

    def test_profile_creation_successful(self):
        """
        Test successful creation of a :class:`profile.Profile` instance.

        Asserts that the created :class:`profile.Profile` instance has the expected attributes.

        :return: None
        :rtype: None
        """

        self.assertEqual(self.profile.user.username, self.USERNAME)
        self.assertEqual(self.profile.user.email, self.USER_EMAIL)
        self.assertEqual(self.profile.favorite_city, self.FAVORITE_CITY)

    def test_profile_delete_successful(self):
        """
        Test successful deletion of a :class:`profile.Profile` instance.

        Asserts that the :class:`profile.Profile` instance is deleted from the database.

        :return: None
        :rtype: None
        """

        self.assertTrue(Profile.objects.filter(user=self.user).exists())
        self.profile.delete()
        self.assertFalse(Profile.objects.filter(user=self.user).exists())

    def test_profile_str(self):
        """
        Test the string representation of a :class:`profile.Profile` instance.

        Asserts that the string representation is as expected.

        :return: None
        :rtype: None
        """

        self.assertEqual(str(self.profile), self.USERNAME)
