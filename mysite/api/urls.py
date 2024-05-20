from django.urls import path
from . import views
from . import view_account
from . import view_playlist

urlpatterns = [
    path(
        "artist/get-all-artists", views.get_all_artists.as_view(), name="artists-view"
    ),
    path(
        "artist/get-all-artist-country",
        views.get_all_artist_country.as_view(),
        name="all-artists-country-view",
    ),
    path(
        "artist/get-artists-by-country",
        views.get_artist_by_country.as_view(),
        name="artists-country-view",
    ),
    path(
        "artist/get-popular-artists",
        views.get_popular_artists.as_view(),
        name="artists-popular-view",
    ),
    path("genre/get-all-genres", views.get_all_genres.as_view(), name="genres-view"),
    path("track/get-all-tracks", views.get_all_tracks.as_view(), name="tracks-view"),
    path(
        "track/get-shuffled-tracks",
        views.get_shuffle_tracks.as_view(),
        name="tracks-shuffled-view",
    ),
    path(
        "track/get-top-trending-tracks",
        views.get_top_trending_tracks.as_view(),
        name="tracks-top-views",
    ),
    path(
        "track/get-tracks-by-artist-id",
        views.get_tracks_by_artist_id.as_view(),
        name="tracks-by-artist",
    ),
    path(
        "track/get-tracks-by-genre-id",
        views.get_tracks_by_genre_id.as_view(),
        name="tracks-by-genre",
    ),
    path("auth/login", view_account.login, name="login"),
    path("auth/signup", view_account.signup, name="signup"),
    path(
        "auth/validate-token",
        view_account.ValidateTokenView.as_view(),
        name="test-token",
    ),
    path(
        "playlist/create-my-playlist",
        view_playlist.create_my_playlist.as_view(),
        name="create-playlist",
    ),
    path(
        "playlist/remove-my-playlist",
        view_playlist.remove_my_playlist.as_view(),
        name="delete-playlist",
    ),
    path(
        "playlist/get-my-playlist",
        view_playlist.get_my_playlist.as_view(),
        name="get-playlist",
    ),
    path(
        "playlist/get-tracks-by-playlist-id",
        view_playlist.get_tracks_by_playlist_id.as_view(),
        name="get-tracks-playlist",
    ),
    path(
        "playlist/get-tracks-recommend-by-playlist-id",
        view_playlist.get_tracks_recommend_by_playlist_id.as_view(),
        name="get-tracks-recommend-playlist",
    ),
    path(
        "playlist/add-track-to-my-playlist",
        view_playlist.add_track_to_my_playlist.as_view(),
        name="add-track-playlist",
    ),
    path(
        "playlist/remove-track-from-my-playlist",
        view_playlist.remove_track_from_my_playlist.as_view(),
        name="remove-track-playlist",
    ),
]
