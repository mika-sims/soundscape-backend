from django.db import IntegrityError
from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'created_at',
            'owner',
            'post'
        ]

    def create(self, validated_data):
        # Handle the case where a user tries to like a post more than once.
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already liked this post.'
            })
