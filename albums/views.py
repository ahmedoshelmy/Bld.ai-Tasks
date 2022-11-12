from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, pagination
from rest_framework.generics import ListAPIView
from .filters import AlbumFilters
import sys


# Create your views here.

class AlbumView(ListAPIView):
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = AlbumSerializer
    get_queryset = Album.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumFilterView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = AlbumFilters

    def get(self, request, *args, **kwargs):
        params = request.query_params
        gte, lte, icontains = 0, sys.maxsize, ''
        if 'cost__gte' in params:
            if params['cost__gte']:
                try:
                    data = int(params['cost__gte'])
                    gte = data
                except:
                    return Response(data={"cost__gte": ["Enter a number."]}, status=status.HTTP_400_BAD_REQUEST)

        if 'cost__lte' in params:
            if params['cost__lte']:
                try:
                    data = int(params['cost__lte'])
                    lte = data
                except:
                    return Response(data={"cost__lte": ["Enter a number."]}, status=status.HTTP_400_BAD_REQUEST)

        if 'name__icontains' in params:
            if params['name__icontains']:
                icontains = params['name__icontains']

        data = Album.objects.filter(cost__gte=gte, cost__lte=lte, name__icontains=icontains)
        serializer = AlbumSerializer(data, many=True)

        if 'limit' not in params:
            return Response(serializer.data)

        return self.get_paginated_response(self.paginate_queryset(serializer.data))
