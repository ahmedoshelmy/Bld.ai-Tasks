from django.contrib import admin
from .models import *
from albums.models import *
from django.db.models import Count


# Register your models here.

class InlineArtistAlbum(admin.TabularInline):
    model = Album
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'album_count', 'social_link', 'approved_albums']
    inlines = [InlineArtistAlbum]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _album_count=Count('album'),
        ).annotate(
            _approved_albums=models.Count('album', filter=models.Q(album__approved=True))
        )
        return queryset

    def album_count(self, obj):
        return obj._album_count

    def approved_albums(self, obj):
        return obj._approved_albums

    album_count.admin_order_field = '_album_count'
    approved_albums.admin_order_field = '_approved_albums'
