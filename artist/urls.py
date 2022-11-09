from django.urls import path
from .views import *

app_name = 'artist'
urlpatterns = [
    path('', ArtistsView.as_view()),
]
