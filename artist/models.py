from django.db import models


# Create your models here.

class Artist(models.Model):
    stage_name = models.CharField(max_length=30, unique=True)
    social_link = models.URLField(blank=True)

    class Meta:
        ordering = ['stage_name']

