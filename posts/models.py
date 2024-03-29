from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model for storing blog posts
    """

    AUDIO_FILE_TYPES = [
        ('recording', 'Recording'),
        ('composition', 'Composition'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.FileField(blank=True)
    audio_type = models.CharField(
        max_length=32,
        choices=AUDIO_FILE_TYPES,
        default=''
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to='post_images/',
        null=True,
        blank=True,
        default='../dml85uj9yqmxekst8gbc'
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
