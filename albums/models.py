from django.db import models
from artist.models import Artist
from datetime import datetime
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator


class Song(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG',
                                     options={'quality': 60})
    audio_file = models.FileField(blank=True, validators=[FileExtensionValidator(['mp3', 'wav'])])


class Album(TimeStampedModel):
    name = models.CharField(default='New Album', max_length=30)
    release_date = models.DateTimeField(blank=False)
    cost = models.DecimalField(decimal_places=2, null=False, max_digits=5)
    author = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True)
    approved = models.BooleanField(default=False)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
