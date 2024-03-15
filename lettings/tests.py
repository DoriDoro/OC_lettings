from django.test import TestCase

from lettings.models import Address, Letting


# ------ Testing of the model instance of lettings app ------
# TODO: deletion of a model instance

class ModelTestCase(TestCase):
    NUMBER = 15
    STREET = 'Test Street'
    CITY = 'Test City'
    STATE = 'Test State'
    ZIP_CODE = 12345
    COUNTRY_ISO_CODE = 56789

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=cls.NUMBER,
            street=cls.STREET,
            city=cls.CITY,
            state=cls.STATE,
            zip_code=cls.ZIP_CODE,
            country_iso_code=cls.COUNTRY_ISO_CODE
        )


class AddressTestCase(ModelTestCase):
    INVALID_NUMBER = 'one'

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
                country_iso_code=self.COUNTRY_ISO_CODE
            )

    def test_address_str(self):
        self.assertEqual(f'{self.address.number} {self.address.street}',
                         f'{self.NUMBER} {self.STREET}')


class LettingTestCase(ModelTestCase):
    TEST_TITLE = 'Test Title'
    TEST_ADDRESS = 'No model instance'

    def test_create_letting_successful(self):
        letting = Letting.objects.create(
            title=self.TEST_TITLE,
            address=self.address
        )

        self.assertEqual(letting.title, self.TEST_TITLE)
        self.assertEqual(letting.address.number, self.NUMBER)
        self.assertEqual(letting.address.street, self.STREET)
        self.assertEqual(letting.address.city, self.CITY)
        self.assertEqual(letting.address.state, self.STATE)

    def test_create_letting_failed(self):
        with self.assertRaises(ValueError):
            Letting.objects.create(
                title=self.TEST_TITLE,
                address=self.TEST_ADDRESS
            )

    def test_letting_str(self):
        letting = Letting.objects.create(
            title=self.TEST_TITLE,
            address=self.address
        )

        self.assertEqual(letting.title, self.TEST_TITLE)
