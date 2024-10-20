# Generated by Django 5.1.1 on 2024-10-16 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_time_of_publication']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time_of_publication',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
    ]
