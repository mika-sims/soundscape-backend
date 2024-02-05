from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        # Check if the user is the owner of the profile
        return obj.owner == self.context['request'].user

    def validate_image(self, value):
        # Validate the profile image size
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size must be less than 2MB'
            )
        if value.image.width > 2048 or value.image.height > 2048:
            raise serializers.ValidationError(
                'Image dimensions must be less than 2048x2048'
            )
        return value

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'is_owner',
            'full_name',
            'bio',
            'image',
            'created_at',
            'updated_at'
        ]
