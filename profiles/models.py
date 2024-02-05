from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    User profile model for maintaining user information
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='images/profile_image',
        default='../default_profile_bxidbs'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"
