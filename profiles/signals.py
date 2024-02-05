from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Signals to create user profile when a new user is created
    if created:
        Profile.objects.create(owner=instance)
