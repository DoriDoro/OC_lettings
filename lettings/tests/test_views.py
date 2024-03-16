from django.http import Http404
from django.test import TestCase, RequestFactory
from django.urls import reverse

from lettings.models import Letting, Address
from lettings.views import index, letting


class LettingViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=18,
            street='Test Street View',
            city='Test City View',
            state='Test State View',
            zip_code=52369,
            country_iso_code=74125
        )

        cls.letting = Letting.objects.create(title='Test House 1', address=cls.address)


class LettingsIndexViewTestCase(TestCase):
    def test_letting_index_view(self):
        request = RequestFactory().get(reverse('lettings:lettings_index'))
        response = index(request)

        self.assertEqual(response.status_code, 200)


class LettingsDetailViewTestCase(LettingViewTestCase):
    def test_letting_id_view_successful(self):
        request = RequestFactory().get(
            reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        )
        response = letting(request, letting_id=self.letting.id)

        self.assertEqual(response.status_code, 200)

    def test_letting_id_view_failed(self):
        request = RequestFactory().get(
            reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        )
        with self.assertRaises(Http404):
            letting(request, letting_id=6)
