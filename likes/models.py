from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class Like(models.Model):
    """
    Like model, related to Post and User models.
    'owner' is the user who liked the post.
    'post' is the post that was liked.
    'unique_together' ensures that a user can only like a post once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
