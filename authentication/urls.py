from django.urls import path
from .views import *
from knox import views as knox_views

app_name = 'authentication'
urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
]
