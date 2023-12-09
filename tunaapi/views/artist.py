from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist

class ViewArtist(ViewSet):
    """artist view"""

    def create(self, request):
        """Handle POST operations for artists
      
        Returns 
            Response -- JSON serialized artist instance
        """
        artist = Artist.objects.create(
          name=request.data["name"],
          age=request.data["age"],
          bio=request.data["bio"],
        )
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArtistSerializer(serializers.ModelSerializer):
    """serializer for artists"""
    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio')
        depth = 1
