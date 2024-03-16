from django.test import TestCase, RequestFactory
from django.urls import reverse

from core.views import index


class CoreViewTestCase(TestCase):
    def test_core_index_view(self):
        request = RequestFactory().get(reverse('core:index'))
        response = index(request)

        self.assertEqual(response.status_code, 200)
