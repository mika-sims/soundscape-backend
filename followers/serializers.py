from django.db import IntegrityError
from rest_framework import serializers

from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    """
    owner = serializers.ReadOnlyField(
        source='owner.username'
    )
    followed_name = serializers.ReadOnlyField(
        source='followed.username'
    )

    class Meta:
        model = Follower
        fields = [
            'id',
            'owner',
            'created_at',
            'followed',
            'followed_name'
        ]

    def create(self, validated_data):
        # Handle the cases where a user tries to follow
        # another user more than once.

        owner = validated_data['owner']
        followed = validated_data['followed']

        # Display user friendly error messages
        # if the user tries to follow themselves
        if owner == followed:
            raise serializers.ValidationError({
                'detail': "You can't follow yourself."
            })

        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already following this user.'
            })
