from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model for storing user following relationships.

    The 'unique_together' is used to enforce a unique constraint
    on a combination of fields. This means that user can't follow
    another user more than once.

    owner = user who is following another user
    followed = user who is followed by another user
    related_name = to distinguish users.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            # Constraints to prevent self folowing
            models.UniqueConstraint(
                fields=['owner', 'followed'], name='unique_followers'
            ),
            models.CheckConstraint(
                check=~models.Q(owner=models.F('followed')),
                name='owner_not_followed'
            )
        ]

    def __str__(self):
        return f'{self.owner} {self.followed}'
