from rest_framework import serializers
from .models import *
from artist.serializers import *
from .tasks import send_mail_task
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class AlbumSerializer(serializers.Serializer):
    name = serializers.CharField(default='New Album', max_length=30)
    release_date = serializers.DateTimeField()
    cost = serializers.DecimalField(decimal_places=2, max_digits=5)
    approved = serializers.BooleanField(default=False)
    song = serializers.IntegerField(required=False)

    def create(self, validated_data):
        send_mail_task()

        return Album.objects.create(**validated_data)


@receiver(post_save, sender=Album)
def album_post_save(sender, instance, created, *args, **kwargs):
    if created:
        send_mail_task.delay(instance.name, instance.artist.id)
