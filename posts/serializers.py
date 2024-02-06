from rest_framework import serializers

from likes.models import Like
from .models import Post
from .custom_serializers import AudioUploadField


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    audio = AudioUploadField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        return obj.owner == self.context['request'].user

    def get_like_id(self, obj):
        # Get the like id if the user has liked the post, else return None
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'audio',
            'audio_type',
            'title',
            'content',
            'image',
            'latitude',
            'longitude',
            'created_at',
            'updated_at',
            'comments_count',
            'like_id',
            'likes_count',
        ]
