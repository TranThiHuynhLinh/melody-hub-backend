from rest_framework import serializers
from .models import Artist
from .models import Genre
from .models import Track
from .models import UserInfor
from .models import AccountRole
from .models import Playlist
from django.contrib.auth.models import User


class UserInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfor
        fields = ["user_id", "username", "avatar_image", "playlist_ids"]


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = [
            "playlist_id",
            "playlist_name",
            "track_ids",
            "recommended_track_ids",
            "user_id",
            "image_url",
        ]


class AccountRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountRole
        fields = ["role_name", "user_name"]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "artist_name", "country", "artist_image"]


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "genre_name"]


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        filter = [
            "id",
            "track_name",
            "artist_id",
            "genre_id",
            "track_url",
            "image_url",
            "duration",
            "release_year",
            "view",
        ]
