from rest_framework import serializers
from cloudinary.uploader import upload
from cloudinary.exceptions import Error as CloudinaryException


class AudioUploadField(serializers.FileField):
    """
    Custom serializer field for uploading audio files to Cloudinary.

    Cloudinary does not accept audio files when using the default
    FileField provided by DRF. Standard DRF serializer fields are not suitable
    for handling Cloudinary-specific requirements for audio file uploads.

    The custom serializer field is created to bridge the gap between
    DRF serializers and Cloudinary's specific requirements
    for handling audio files during the upload process.
    """

    def to_internal_value(self, data):
        """
        Upload the audio file to Cloudinary and return the file URL.
        """

        try:
            audio = upload(
                data,
                resource_type='',
                folder = 'audio/',
                format='mp3',
            )
            return audio['secure_url']
        except CloudinaryException as e:
            raise serializers.ValidationError(e.message)
        except Exception as e:
            raise serializers.ValidationError(e)
