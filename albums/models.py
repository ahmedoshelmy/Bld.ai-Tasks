from django.db import models
from artist.models import Artist


# Create your models here.

class Album(models.Model):
    name = models.CharField(default='New Album', max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    release_date = models.DateTimeField(blank=False)
    cost = models.DecimalField(decimal_places=2, null=False)
    author = models.ForeignKey(Artist, on_delete=models.CASCADE)
