from django.core.exceptions import ValidationError


def validate_photo_file_size(image):
    if image.size > 5 * 1024 * 1024:
        raise ValidationError('The image size should not exceed 5MB')
