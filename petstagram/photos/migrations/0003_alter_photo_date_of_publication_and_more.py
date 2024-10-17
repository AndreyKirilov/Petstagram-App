# Generated by Django 5.1.1 on 2024-10-17 11:04

import django.core.validators
import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_rename_photo_pet_personal_photo_alter_pet_slug'),
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_of_publication',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', validators=[petstagram.photos.validators.FileSizeValidator(5)]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, to='pets.pet'),
        ),
    ]
