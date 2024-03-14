"""
Test module for profiles app models.
"""

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

from profiles.models import Profile

UserModel = get_user_model()


class ModelTestCase(TestCase):
    """
    Base test case for model testing.
    """

    USERNAME = 'Test User'
    USER_EMAIL = 'john.doe@mail.com'
    USER_PASSWORD = 'TestPassword'
    USER_FIRST_NAME = 'John'
    USER_LAST_NAME = 'Doe'

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the base model test case.
        """

        cls.user = UserModel.objects.create_user(
            username=cls.USERNAME,
            password=cls.USER_PASSWORD,
            email=cls.USER_EMAIL,
            first_name=cls.USER_FIRST_NAME,
            last_name=cls.USER_LAST_NAME,
        )


class ProfileTestCase(ModelTestCase):
    """
    Test case for Profile model.
    """

    def test_user_creation_successful(self):
        """
        Test successful user creation.
        """

        test_username = 'Test Profile User'
        test_email = 'jane.doe@mail.com'
        test_first_name = 'Jane'
        test_last_name = 'Doe'

        user = UserModel.objects.create_user(
            username=test_username,
            password=self.USER_PASSWORD,
            email=test_email,
            first_name=test_first_name,
            last_name=test_last_name,
        )
        self.assertEqual(user.username, test_username)
        self.assertEqual(user.email, test_email)
        self.assertEqual(user.first_name, test_first_name)
        self.assertEqual(user.last_name, test_last_name)

    def test_user_creation_failed(self):
        """
        Test user creation with invalid data.
        """

        invalid_data = [
            {'username': '', "email": "", "password": None},
            {'username': '', "email": None, "password": ''},
            {'username': '', "email": "testuser1@mail.com", "password": ""},
            {'username': '', "email": "testuser2@mail.com", "password": None},
            {'username': '', "email": '', "password": self.USER_PASSWORD},
            {'username': '', "email": None, "password": self.USER_PASSWORD},
        ]

        for data in invalid_data:
            with self.assertRaises(ValueError):
                UserModel.objects.create_user(**data)

    def test_user_creation_second_time(self):
        """
        Test user creation when the user already exists.
        """

        with self.assertRaises(IntegrityError):
            UserModel.objects.create_user(
                username=self.USERNAME,
                password=self.USER_PASSWORD,
                email=self.USER_EMAIL,
                first_name=self.USER_FIRST_NAME,
                last_name=self.USER_LAST_NAME,
            )

    def test_profile_creation_successful(self):
        """
        Test successful profile creation.
        """

        favorite_city = 'Rennes'

        profile = Profile.objects.create(
            user=self.user,
            favorite_city=favorite_city
        )

        self.assertEqual(profile.user.username, self.USERNAME)
        self.assertEqual(profile.user.email, self.USER_EMAIL)
        self.assertEqual(profile.favorite_city, favorite_city)

    def test_profile_str(self):
        """
        Test string representation of the profile.
        """

        self.assertEqual(self.user.username, self.USERNAME)




