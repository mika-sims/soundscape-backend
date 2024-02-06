from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from config.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    """
    View for retrieving a list of comments or 
    creating a new comment if the user is authenticated

    owner = username of the post owner
    is_owner = true if the user is the owner of the post
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating or deleting a comment

    owner = username of the post owner
    is_owner = true if the user is the owner of the post
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
