from django.contrib import admin
from .models import *
from django.db.models import Count


# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'album_count', 'social_link']

