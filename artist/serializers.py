from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.Serializer):
    stage_name = serializers.CharField(max_length=30)
    social_link = serializers.URLField()

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)
