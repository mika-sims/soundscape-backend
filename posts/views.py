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
    profile_id = id of the profile of the post owner
    profile_image = url of the profile image of the post owner
    created_at = natural time or date of the post creation
    updated_at = natural time or date of the post update
    """
    
    queryset = Post.objects.all()
    
    serializer_class = PostSerializer
    
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)