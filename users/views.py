from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .permissions import *


# Create your views here.

class UserView(APIView):
    permission_classes = [SameUser]

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(User, pk=kwargs['id'])
        serializer = UserSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        obj = User.objects.get(pk=kwargs['id'])
        data = request.data
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def patch(self, request, *args, **kwargs):
        obj = User.objects.get(pk=kwargs['id'])
        data = request.data
        serializer = UserSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)
