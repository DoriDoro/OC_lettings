"""
Module to test models of the lettings app.

This module contains test cases for the models defined in the lettings app. It includes
test cases for the Address and Letting models.

Attributes:
    TestCase: A subclass of Django's TestCase class for writing unit tests.
    ValueError: An exception is often raised in Python when an invalid value is assigned to a
    variable or passed to a function while calling it.

Classes:
    ModelTestCase(TestCase): A base test case class for setting up common test data.
    AddressTestCase(ModelTestCase): Test case class for testing the Address model.
    LettingTestCase(ModelTestCase): Test case class for testing the Letting model.

Methods:
    setUpTestData: Method to set up test data for the Address model.
    test_address_creation_successful: Method to test successful creation of an Address instance.
    test_address_creation_failed: Method to test failed creation of an Address instance.
    test_address_str: Method to test the string representation of an Address instance.
    test_address_delete_successful: Method to test successful deletion of an Address instance.
    setUp: Method to set up test data for the Letting model.
    test_letting_create_successful: Method to test successful creation of a Letting instance.
    test_letting_create_failed: Method to test failed creation of a Letting instance.
    test_letting_delete_successful: Method to test successful deletion of a Letting instance.
    test_letting_str: Method to test the string representation of a Letting instance.
"""

from django.test import TestCase

from lettings.models import Address, Letting


class ModelTestCase(TestCase):
    NUMBER = 15
    STREET = "Test Street"
    CITY = "Test City"
    STATE = "TE"
    ZIP_CODE = 12345
    COUNTRY_ISO_CODE = 789

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=cls.NUMBER,
            street=cls.STREET,
            city=cls.CITY,
            state=cls.STATE,
            zip_code=cls.ZIP_CODE,
            country_iso_code=cls.COUNTRY_ISO_CODE,
        )


class AddressTestCase(ModelTestCase):
    INVALID_NUMBER = "one"

    def test_address_creation_successful(self):
        self.assertEqual(self.address.number, self.NUMBER)
        self.assertEqual(self.address.street, self.STREET)
        self.assertEqual(self.address.city, self.CITY)

    def test_address_creation_failed(self):
        with self.assertRaises(ValueError):
            Address.objects.create(
                number=self.INVALID_NUMBER,
                street=self.STREET,
                city=self.CITY,
                state=self.STATE,
                zip_code=self.ZIP_CODE,
                country_iso_code=self.COUNTRY_ISO_CODE,
            )

    def test_address_str(self):
        self.assertEqual(str(self.address), f"{self.NUMBER} {self.STREET}")

    def test_address_delete_successful(self):
        self.assertTrue(Address.objects.filter(number=self.address.number).exists())
        self.address.delete()
        self.assertFalse(Address.objects.filter(number=self.address.number).exists())


class LettingTestCase(ModelTestCase):
    TEST_TITLE = "Test Title"
    TEST_ADDRESS = "No model instance"

    def setUp(self):
        super().setUp()
        self.letting = Letting.objects.create(
            title=self.TEST_TITLE, address=self.address
        )

    def test_letting_create_successful(self):
        self.assertEqual(self.letting.title, self.TEST_TITLE)
        self.assertEqual(self.letting.address.number, self.NUMBER)
        self.assertEqual(self.letting.address.street, self.STREET)
        self.assertEqual(self.letting.address.city, self.CITY)
        self.assertEqual(self.letting.address.state, self.STATE)

    def test_letting_create_failed(self):
        with self.assertRaises(ValueError):
            Letting.objects.create(title=self.TEST_TITLE, address=self.TEST_ADDRESS)

    def test_letting_delete_successful(self):
        self.assertTrue(Letting.objects.filter(title=self.letting.title).exists())
        self.letting.delete()
        self.assertFalse(Letting.objects.filter(title=self.letting.title).exists())

    def test_letting_str(self):
        self.assertEqual(str(self.letting), self.TEST_TITLE)
