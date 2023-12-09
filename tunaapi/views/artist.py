"""views for handling requests"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist
from django.db.models import Count

class ViewArtist(ViewSet):
    """artist view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single artist
      
        Returns:
          Response -- JSON serialized artist
        """
        try:
            artist = Artist.objects.annotate(song_count=Count('songs')).get(pk=pk)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Artist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all artists
        
        Return:
            Response -- JSON serialized list for artists
        """
        artists = Artist.objects.annotate(song_count=Count('songs')).all()

        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

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

    def update(self, request, pk):
        """Handle PUT requests for an artist
      
        Returns:
            Reponse -- Empty body with 204 status code
        """
        artist = Artist.objects.get(pk=pk)
        artist.name = request.data["name"]
        artist.age = request.data["age"]
        artist.bio = request.data["bio"]

        artist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE request for an artist"""
        artist = Artist.objects.get(pk=pk)
        artist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ArtistSerializer(serializers.ModelSerializer):
    """serializer for artists"""
    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio', 'song_count', 'songs')
        depth = 1
