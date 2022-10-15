from django.db import models


# Create your models here.

class Artist(models.Model):
    stage_name = models.CharField(max_length=30, unique=True)
    social_link = models.URLField(blank=True)

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ['stage_name']

