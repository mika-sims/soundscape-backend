from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from .models import Profile
from .serializers import ProfileSerializer
from followers.models import Follower


class ProfileModelTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='password')

    def test_str_method(self):
        testuser = User.objects.get(username='testuser')
        profile = Profile.objects.get(owner=testuser)
        self.assertEqual(str(profile), f"{testuser}'s profile")


class ProfileSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.profile = Profile.objects.get(owner=self.user)
        self.otheruser = User.objects.create_user(
            username='otheruser', password='otherpassword')
        self.otherprofile = Profile.objects.get(owner=self.otheruser)
        self.client = APIClient()

    def test_get_is_owner_returns_true(self):
        self.client.login(username='testuser', password='testpassword')
        request = APIRequestFactory().get('/')
        request.user = self.user
        serializer = ProfileSerializer(
            self.profile, context={'request': request})
        self.assertTrue(serializer.get_is_owner(self.profile))

    def test_get_is_owner_returns_false(self):
        self.client.login(username='testuser', password='testpassword')
        request = APIRequestFactory().get('/')
        request.user = self.otheruser
        serializer = ProfileSerializer(
            self.profile, context={'request': request})
        self.assertFalse(serializer.get_is_owner(self.profile))

    def test_get_following_id_method_returns_follow_id(self):
        self.client.login(username="testuser", password="testpassword")
        follow = Follower.objects.create(
            owner=self.user, followed=self.otheruser)
        request = APIRequestFactory().get('/')
        request.user = self.user
        serializer = ProfileSerializer(
            self.profile, context={'request': request})
        self.assertEqual(serializer.get_following_id(
            self.otherprofile), follow.id)

