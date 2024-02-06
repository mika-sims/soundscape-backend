from django.contrib import admin

from .models import Comment


# Register the comment model with the admin site
admin.site.register(Comment)
