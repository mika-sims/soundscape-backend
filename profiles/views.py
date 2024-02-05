from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from config.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    
    owner = username of the profile owner
    is_owner = true if the user is the owner of the profile
    """
    
    queryset = Profile.objects.all()
    
    serializer_class = ProfileSerializer