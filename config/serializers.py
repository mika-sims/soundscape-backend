from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Custom serializer for the current user, extending UserDetailsSerializer
    Additional read-only fields to include profile information
    in the user's details
    """

    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        # Include the fields from the parent UserDetailsSerializer.Meta.fields
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
