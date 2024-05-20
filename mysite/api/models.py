from django.db import models


class Artist(models.Model):
    artist_id = models.CharField(primary_key=True, max_length=1000)
    artist_name = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    artist_image = models.TextField()

    def __str__(self):
        return self.artist_name

    def get_artist_name_by_id(self, artist_id):
        try:
            artist = Artist.objects.get(pk=artist_id)
            return artist.artist_name
        except Artist.DoesNotExist:
            return None


class Genre(models.Model):
    genre_id = models.CharField(primary_key=True, max_length=1000)
    genre_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.genre_name

    def get_genre_name_by_id(self, genre_id):
        try:
            genre = Genre.objects.get(pk=genre_id)
            return genre.genre_name
        except Genre.DoesNotExist:
            return None


class Track(models.Model):
    track_name = models.CharField(max_length=10000)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    track_url = models.TextField()
    image_url = models.TextField()
    duration = models.IntegerField()
    release_year = models.IntegerField()
    view = models.IntegerField()

    def __str__(self):
        return self.track_name


class UserInfor(models.Model):
    user_id = models.CharField(primary_key=True, max_length=1000)
    username = models.CharField(max_length=1000)
    avatar_image = models.TextField()
    playlist_ids = models.TextField()  # list of playlists

    def __str__(self):
        return self.username


class AccountRole(models.Model):
    role_name = models.CharField(max_length=1000)
    user_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.role


class Playlist(models.Model):
    playlist_id = models.CharField(primary_key=True, max_length=1000)
    playlist_name = models.CharField(max_length=1000)
    user_id = models.ForeignKey(UserInfor, on_delete=models.CASCADE)
    track_ids = models.TextField()  # list of tracks
    recommended_track_ids = models.TextField()  # list of tracks
    total_duration = models.IntegerField()
    image_url = models.TextField()

    def __str__(self):
        return self.playlist_name
