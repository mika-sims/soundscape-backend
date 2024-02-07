from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from django.contrib.auth.models import User

from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post


class CommentModelTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='password')

    def test_str_method(self):
        testuser = User.objects.get(username='testuser')
        post = Post.objects.create(
            owner=testuser,
            content='test content',
            latitude=123.456,
            longitude=123.456,
        )
        comment = Comment.objects.create(
            owner=testuser,
            post=post,
            content='test content'
        )
        self.assertEqual(str(comment), comment.content)
