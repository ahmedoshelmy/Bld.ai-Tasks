from rest_framework import serializers
from .models import *
from artist.serializers import *


class AlbumSerializer(serializers.Serializer):
    name = serializers.CharField(default='New Album', max_length=30)
    release_date = serializers.DateTimeField()
    cost = serializers.DecimalField(decimal_places=2, max_digits=5)
    approved = serializers.BooleanField(default=False)
    song = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
