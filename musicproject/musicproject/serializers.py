from .models import Album, Song
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):
    class Meta :
        model = Album
        field = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta :
        model = Song
        field =('album', song_title)