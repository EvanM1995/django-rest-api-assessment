from django.db import models
from .song import Song
from .genre import Genre


class SongGenre(models.Model):

    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='genres')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='song_genres')
