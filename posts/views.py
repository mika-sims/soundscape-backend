from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from config.permissions import IsOwnerOrReadOnly

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all posts or create a new post.

    owner = username of the post owner
    is_owner = true if the user is the owner of the post
    """

    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    ordering_fields = [
        'comments_count',
    ]

    serializer_class = PostSerializer

    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post.

    owner = username of the post owner
    is_owner = true if the user is the owner of the post
    """

    permission_classes = [IsOwnerOrReadOnly]

    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    serializer_class = PostSerializer
