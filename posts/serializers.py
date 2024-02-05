from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime
from datetime import timedelta
from rest_framework import serializers

from .models import Post
from .custom_serializers import AudioUploadField


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for post model
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    audio = AudioUploadField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        return obj.owner == self.context["request"].user

    def get_created_at(self, obj):
        if obj.created_at > timezone.now() - timedelta(days=1):
            return naturaltime(obj.created_at)
        else:
            return obj.created_at.strftime("%d %b %Y, %I:%M %p")

    def get_updated_at(self, obj):
        if obj.updated_at > timezone.now() - timedelta(days=1):
            return naturaltime(obj.updated_at)
        else:
            return obj.updated_at.strftime("%d %b %Y, %I:%M %p")
        
    
    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "audio",
            "audio_type",
            "title",
            "content",
            "image",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
        ]