from django.shortcuts import render
from .models import Album,Song
from rest_framework import viewsets
from .serializers import AlbumSerializer,SongSerializer
# Create your views here.

class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all() 
    serializers_class = AlbumSerializer

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all() 
    serializers_class = SongSerializer