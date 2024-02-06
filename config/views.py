from rest_framework.decorators import api_view
from rest_framework.response import Response

from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def soundscape_rest_api(request):
    return Response({
        'message': 'Welcome to the Soundscape REST API!',
        'API endpoints': {
            'profiles': 'soundscape/api/profiles',
            'profile_detail': 'soundscape/api/profiles/:id',
            'posts': 'soundscape/api/posts',
            'post_detail': 'soundscape/api/posts/:id',
            'followers': 'soundscape/api/followers',
            'follower_detail': 'soundscape/api/followers/:id',
            'comments': 'soundscape/api/comments',
            'comment_detail': 'soundscape/api/comments/:id',
            'likes': 'soundscape/api/likes',
            'like_detail': 'soundscape/api/likes/:id',
        },
        'GitHub Repo': 'https://github.com/mika-sims/soundscape-backend',
    })


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
