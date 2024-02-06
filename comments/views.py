from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    """
    View for retrieving a list of comments or 
    creating a new comment if the user is authenticated
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
