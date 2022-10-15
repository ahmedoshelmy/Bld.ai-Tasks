from django.contrib import admin

# Register your models here.
from .models import *
from .forms import *


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ['creation_date']
    form = AlbumForm
