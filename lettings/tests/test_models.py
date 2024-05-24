"""
Module to test models of the lettings app.

This module contains test cases for the models defined in the lettings app. It includes
test cases for the :class:`lettings.Address` and :class:`lettings.Letting` models.

Attributes:
    TestCase (TestCase): A subclass of Django's TestCase class for writing unit tests.
    ValueError (Exception): An exception raised in Python when an invalid value is assigned
                            to a variable or passed to a function.

Classes:
    ModelTestCase (TestCase): A base test case class for setting up common test data.
    AddressTestCase (ModelTestCase): Test case class for testing the :class:`lettings.Address` model.
    LettingTestCase (ModelTestCase): Test case class for testing the :class:`lettings.Letting` model.

Methods:
    ModelTestCase.setUpTestData: Method to set up test data for the :class:`lettings.Address` model.
    AddressTestCase.test_address_creation_successful: Method to test successful creation of an
    :class:`lettings.Address` instance.
    AddressTestCase.test_address_creation_failed: Method to test failed creation of an :class:`lettings.Address`
    instance.
    AddressTestCase.test_address_str: Method to test the string representation of an :class:`lettings.Address`
    instance.
    AddressTestCase.test_address_delete_successful: Method to test successful deletion of an
    :class:`lettings.Address` instance.
    LettingTestCase.setUp: Method to set up test data for the :class:`lettings.Letting` model.
    LettingTestCase.test_letting_create_successful: Method to test successful creation of a
    :class:`lettings.Letting` instance.
    LettingTestCase.test_letting_create_failed: Method to test failed creation of a :class:`lettings.Letting`
    instance.
    LettingTestCase.test_letting_delete_successful: Method to test successful deletion of a
    :class:`lettings.Letting` instance.
    LettingTestCase.test_letting_str: Method to test the string representation of a :class:`lettings.Letting`
    instance.

:param TestCase: A subclass of Django's TestCase class for writing unit tests.
"""

from django.test import TestCase

from lettings.models import Address, Letting


class ModelTestCase(TestCase):
    """
    Base test case class for setting up common test data.

    Methods:
        setUpTestData: Method to set up test data before running tests.

    :param NUMBER: Test number for the :class:`lettings.Address`.
    :type NUMBER: int, required
    :param STREET: Test street for the :class:`lettings.Address`.
    :type STREET: str, required
    :param CITY: Test city for the :class:`lettings.Address`.
    :type CITY: str, required
    :param STATE: Test state for the :class:`lettings.Address`.
    :type STATE: str, required
    :param ZIP_CODE: Test zip code for the :class:`lettings.Address`.
    :type ZIP_CODE: int, required
    :param COUNTRY_ISO_CODE: Test country ISO code for the :class:`lettings.Address`.
    :type COUNTRY_ISO_CODE: int, required
    :param address: An instance of Address model.
    :type address: class:`lettings.Address`
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
        Set up test data for the :class:`lettings.Address` model.

        Creates an :class:`lettings.Address` instance with predefined test data.

        :param number: An attribute of an instance of :class:`lettings.Address` model.
        :type number: int, required
        :param street: An attribute of an instance of :class:`lettings.Address` model.
        :type street: str, required
        :param city: An attribute of an instance of :class:`lettings.Address` model.
        :type city: str, required
        :param state: An attribute of an instance of :class:`lettings.Address` model.
        :type state: str, required
        :param zip_code: An attribute of an instance of :class:`lettings.Address` model.
        :type zip_code: int, required
        :param country_iso_code: An attribute of an instance of :class:`lettings.Address` model.
        :type country_iso_code: int, required
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
    Test case class for testing the :class:`lettings.Address` model and it inherits from ModelTestCase.

    Methods:
        test_address_creation_successful: Method to test the successful creation of an :class:`lettings.Address`
        instance.
        test_address_creation_failed: Method to test the failed creation of an :class:`lettings.Address` instance.
        test_address_str: Method to test the string representative of the :class:`lettings.Address` instance.
        test_address_delete_successful: Method to test the successful deletion of an :class:`lettings.Address` instance.

    :param INVALID_NUMBER (str): Invalid number for testing failed creation.
    :type INVALID_NUMBER: str, required
    """

    INVALID_NUMBER = "one"

    def test_address_creation_successful(self):
        """
        Test successful creation of an Address instance.

        Asserts that the created Address instance has the expected attributes.

        :return: None
        :rtype: None
        """

        self.assertEqual(self.address.number, self.NUMBER)
        self.assertEqual(self.address.street, self.STREET)
        self.assertEqual(self.address.city, self.CITY)

    def test_address_creation_failed(self):
        """
        Test failed creation of an :class:`lettings.Address` instance.

        Asserts that a ValueError is raised when an invalid number is used.

        :raises ValueError: If an invalid number is used for creating an :class:`lettings.Address`.
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
        Test the string representation of an :class:`lettings.Address` instance.

        Asserts that the string representation is as expected.

        :return: None
        :rtype: None
        """

        self.assertEqual(str(self.address), f"{self.NUMBER} {self.STREET}")

    def test_address_delete_successful(self):
        """
        Test successful deletion of an :class:`lettings.Address` instance.

        Asserts that the :class:`lettings.Address` instance is deleted from the database.

        :return: None
        :rtype: None
        """

        self.assertTrue(Address.objects.filter(number=self.address.number).exists())
        self.address.delete()
        self.assertFalse(Address.objects.filter(number=self.address.number).exists())


class LettingTestCase(ModelTestCase):
    """
    Test case class for testing the :class:`lettings.Letting` model.

    Methods:
        setUp: Method to set up test data before running tests.
        test_letting_create_successful: Method to test the successful creation of a :class:`lettings.Letting` instance.
        test_letting_create_failed: Method to test the failed creation of a :class:`lettings.Letting` instance.
        test_letting_delete_successful: Method to test the successful deletion of a :class:`lettings.Letting` instance.
        test_letting_str: Method to test the string representative of the :class:`lettings.Letting` instance.

    :param TEST_TITLE: A string representative the test_title for test :class:`lettings.Letting` instance.
    :type TEST_TITLE: str, required
    :param TEST_ADDRESS: A string representative the test_address for test :class:`lettings.Letting` instance.
    :type TEST_ADDRESS: str, required
    :param letting: An instance of :class:`lettings.Letting` model.
    :type letting: class:`lettings.Letting`
    """

    TEST_TITLE = "Test Title"
    TEST_ADDRESS = "No model instance"

    def setUp(self):
        """
        Set up test data for the :class:`lettings.Letting` model.

        Creates a :class:`lettings.Letting` instance with the predefined test data.

        :param title: An attribute of an instance of :class:`lettings.Letting` model.
        :type title: str, required
        :param address: An instance of :class:`lettings.Address` model.
        :type address: class:`lettings.Address`
        """

        super().setUp()
        self.letting = Letting.objects.create(
            title=self.TEST_TITLE, address=self.address
        )

    def test_letting_create_successful(self):
        """
        Test successful creation of a :class:`lettings.Letting` instance.

        Asserts that the created :class:`lettings.Letting` instance has the expected attributes.

        :return: None
        :rtype: None
        """

        self.assertEqual(self.letting.title, self.TEST_TITLE)
        self.assertEqual(self.letting.address.number, self.NUMBER)
        self.assertEqual(self.letting.address.street, self.STREET)
        self.assertEqual(self.letting.address.city, self.CITY)
        self.assertEqual(self.letting.address.state, self.STATE)

    def test_letting_create_failed(self):
        """
        Test failed creation of a :class:`lettings.Letting` instance.

        Asserts that a ValueError is raised when an invalid address is used.

        :raises ValueError: If an invalid address is used for creating a :class:`lettings.Letting`.
        """

        with self.assertRaises(ValueError):
            Letting.objects.create(title=self.TEST_TITLE, address=self.TEST_ADDRESS)

    def test_letting_delete_successful(self):
        """
        Test successful deletion of a :class:`lettings.Letting` instance.

        Asserts that the :class:`lettings.Letting` instance is deleted from the database.

        :return: None
        :rtype: None
        """
        self.assertTrue(Letting.objects.filter(title=self.letting.title).exists())
        self.letting.delete()
        self.assertFalse(Letting.objects.filter(title=self.letting.title).exists())

    def test_letting_str(self):
        """
        Test the string representation of a :class:`lettings.Letting` instance.

        Asserts that the string representation is as expected.

        :return: None
        :rtype: None
        """

        self.assertEqual(str(self.letting), self.TEST_TITLE)
