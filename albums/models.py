from django.db import models
from artist.models import Artist
from datetime import datetime


# Create your models here.

class Album(models.Model):
    name = models.CharField(default='New Album', max_length=30)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    release_date = models.DateTimeField(blank=False)
    cost = models.DecimalField(decimal_places=2, null=False, max_digits=5)
    author = models.ForeignKey(Artist, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
