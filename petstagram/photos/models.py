from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_photo_file_size

# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(validators=[validate_photo_file_size])
    description = models.CharField(max_length=300, blank=True, null=True, validators=[MinLengthValidator(10)])
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True, related_name='pets_photos')
    date_of_publication = models.DateField(auto_now=True)

    def __str__(self):
        return self.description
