from django.urls import path
from .views import *

app_name = 'albums'
urlpatterns = [
    path('', AlbumFilterView.as_view()),
]
