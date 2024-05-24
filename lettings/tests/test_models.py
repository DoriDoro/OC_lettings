"""
Module to test models of the lettings app.

This module contains test cases for the models defined in the lettings app. It includes
test cases for the Address and Letting models.

Attributes:
    TestCase (TestCase): A subclass of Django's TestCase class for writing unit tests.
    ValueError (Exception): An exception raised in Python when an invalid value is assigned
                            to a variable or passed to a function.

Classes:
    ModelTestCase: A base test case class for setting up common test data.
    AddressTestCase: Test case class for testing the Address model.
    LettingTestCase: Test case class for testing the Letting model.

Methods:
    ModelTestCase.setUpTestData: Method to set up test data for the Address model.
    AddressTestCase.test_address_creation_successful: Method to test successful creation of an
    Address instance.
    AddressTestCase.test_address_creation_failed: Method to test failed creation of an Address
    instance.
    AddressTestCase.test_address_str: Method to test the string representation of an Address
    instance.
    AddressTestCase.test_address_delete_successful: Method to test successful deletion of an
    Address instance.
    LettingTestCase.setUp: Method to set up test data for the Letting model.
    LettingTestCase.test_letting_create_successful: Method to test successful creation of a
    Letting instance.
    LettingTestCase.test_letting_create_failed: Method to test failed creation of a Letting
    instance.
    LettingTestCase.test_letting_delete_successful: Method to test successful deletion of a
    Letting instance.
    LettingTestCase.test_letting_str: Method to test the string representation of a Letting
    instance.

:param TestCase: A subclass of Django's TestCase class for writing unit tests.
"""

from django.test import TestCase

from lettings.models import Address, Letting


class ModelTestCase(TestCase):
    """
    Base test case class for setting up common test data.

    Attributes:
        NUMBER (int): Test number for the address.
        STREET (str): Test street for the address.
        CITY (str): Test city for the address.
        STATE (str): Test state for the address.
        ZIP_CODE (int): Test zip code for the address.
        COUNTRY_ISO_CODE (int): Test country ISO code for the address.
        address (Address): An instance of Address model.

    Methods:
        setUpTestData: Method to set up test data before running tests.
    """

    NUMBER = 15
    STREET = "Test Street"
    CITY = "Test City"
    STATE = "TE"
    ZIP_CODE = 12345
    COUNTRY_ISO_CODE = 789

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the Address model.

        Creates an Address instance with predefined test data.

        Attributes:
            number (int): An attribute of an instance of Address model.
            street (str): An attribute of an instance of Address model.
            city (str): An attribute of an instance of Address model.
            state (str): An attribute of an instance of Address model.
            zip_code (int): An attribute of an instance of Address model.
            country_iso_code (int): An attribute of an instance of Address model.
        """

        cls.address = Address.objects.create(
            number=cls.NUMBER,
            street=cls.STREET,
            city=cls.CITY,
            state=cls.STATE,
            zip_code=cls.ZIP_CODE,
            country_iso_code=cls.COUNTRY_ISO_CODE,
        )


class AddressTestCase(ModelTestCase):
    """
    Test case class for testing the Address model.

    Attributes:
        INVALID_NUMBER (str): Invalid number for testing failed creation.

    Methods:
        test_address_creation_successful: Method to test the successful creation of an Address instance.
        test_address_creation_failed: Method to test the failed creation of an Address instance.
        test_address_str: Method to test the string representative of the Address instance.
        test_address_delete_successful: Method to test the successful deletion of an Address instance.
    """

    INVALID_NUMBER = "one"

    def test_address_creation_successful(self):
        """
        Test successful creation of an Address instance.

        Asserts that the created Address instance has the expected attributes.
        """

        self.assertEqual(self.address.number, self.NUMBER)
        self.assertEqual(self.address.street, self.STREET)
        self.assertEqual(self.address.city, self.CITY)

    def test_address_creation_failed(self):
        """
        Test failed creation of an Address instance.

        Asserts that a ValueError is raised when an invalid number is used.

        :raises ValueError: If an invalid number is used for creating an Address.
        """

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
        """
        Test the string representation of an Address instance.

        Asserts that the string representation is as expected.
        """

        self.assertEqual(str(self.address), f"{self.NUMBER} {self.STREET}")

    def test_address_delete_successful(self):
        """
        Test successful deletion of an Address instance.

        Asserts that the Address instance is deleted from the database.
        """

        self.assertTrue(Address.objects.filter(number=self.address.number).exists())
        self.address.delete()
        self.assertFalse(Address.objects.filter(number=self.address.number).exists())


class LettingTestCase(ModelTestCase):
    """
    Test case class for testing the Letting model.

    Attributes:
        TEST_TITLE (str): Test title for the letting.
        TEST_ADDRESS (str): Invalid address for testing failed creation.

    Methods:
        setUp: Method to set up test data before running tests.
        test_letting_create_successful: Method to test the successful creation of a Letting instance.
        test_letting_create_failed: Method to test the failed creation of a Letting instance.
        test_letting_delete_successful: Method to test the successful deletion of a Letting instance.
        test_letting_str: Method to test the string representative of the Letting instance.

    Attributes:
        TEST_TITLE (str): A string representative the test_title for test letting.
        TEST_ADDRESS (str): A string representative the test_address for test letting.
        letting (Letting): An instance of Letting model.
    """

    TEST_TITLE = "Test Title"
    TEST_ADDRESS = "No model instance"

    def setUp(self):
        """
        Set up test data for the Letting model.

        Creates a Letting instance with the predefined test data.

        Attributes:
            title (str): An attribute of an instance of Letting model.
            address (Address): An instance of Address model.
        """

        super().setUp()
        self.letting = Letting.objects.create(
            title=self.TEST_TITLE, address=self.address
        )

    def test_letting_create_successful(self):
        """
        Test successful creation of a Letting instance.

        Asserts that the created Letting instance has the expected attributes.
        """

        self.assertEqual(self.letting.title, self.TEST_TITLE)
        self.assertEqual(self.letting.address.number, self.NUMBER)
        self.assertEqual(self.letting.address.street, self.STREET)
        self.assertEqual(self.letting.address.city, self.CITY)
        self.assertEqual(self.letting.address.state, self.STATE)

    def test_letting_create_failed(self):
        """
        Test failed creation of a Letting instance.

        Asserts that a ValueError is raised when an invalid address is used.

        :raises ValueError: If an invalid address is used for creating a Letting.
        """

        with self.assertRaises(ValueError):
            Letting.objects.create(title=self.TEST_TITLE, address=self.TEST_ADDRESS)

    def test_letting_delete_successful(self):
        """
        Test successful deletion of a Letting instance.

        Asserts that the Letting instance is deleted from the database.
        """
        self.assertTrue(Letting.objects.filter(title=self.letting.title).exists())
        self.letting.delete()
        self.assertFalse(Letting.objects.filter(title=self.letting.title).exists())

    def test_letting_str(self):
        """
        Test the string representation of a Letting instance.

        Asserts that the string representation is as expected.
        """

        self.assertEqual(str(self.letting), self.TEST_TITLE)
