from django_filters import rest_framework as filters

from .models import Album


class AlbumFilters(filters.FilterSet):
    class Meta:
        model = Album
        fields = {
            'cost': ['gte', 'lte'],
            'name': ['icontains']
        }
