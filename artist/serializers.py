from rest_framework import serializers


class ArtistSerializer(serializers.Serializer):
    stage_name = serializers.CharField(max_length=30)
    social_link = serializers.URLField()
