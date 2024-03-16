from django.contrib.auth import get_user_model
from django.http import Http404
from django.test import TestCase, RequestFactory
from django.urls import reverse

from profiles.models import Profile
from profiles.views import index, profile

UserModel = get_user_model()


class ProfileViewTestCase(TestCase):
    USERNAME = 'Test User'
    USER_EMAIL = 'john.doe@mail.com'
    USER_PASSWORD = 'TestPassword'
    USER_FIRST_NAME = 'John'
    USER_LAST_NAME = 'Doe'

    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(
            username=cls.USERNAME,
            password=cls.USER_PASSWORD,
            email=cls.USER_EMAIL,
            first_name=cls.USER_FIRST_NAME,
            last_name=cls.USER_LAST_NAME,
        )

        cls.profile = Profile.objects.create(user=cls.user, favorite_city='Test City')


class ProfileIndexViewTestCase(TestCase):
    def test_profile_index_view(self):
        request = RequestFactory().get(reverse('profiles:profiles_index'))
        response = index(request)

        self.assertEqual(response.status_code, 200)


class ProfileDetailViewTestCase(ProfileViewTestCase):
    def test_profile_id_view_successful(self):
        request = RequestFactory().get(
            reverse('profiles:profile', kwargs={'username': self.profile.user.username})
        )
        response = profile(request, username=self.profile.user.username)

        self.assertEqual(response.status_code, 200)

    def test_profile_id_view_failed(self):
        request = RequestFactory().get(
            reverse('profiles:profile', kwargs={'username': self.profile.user.username})
        )

        with self.assertRaises(Http404):
            profile(request, username='Invalid Test Username')
