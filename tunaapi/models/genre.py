from django.db import models


class Genre(models.Model):

    description = models.CharField(max_length=300)

    def songs(self):
        return [song_genre.song_id for song_genre in self.song_genres.all()]
