from django.shortcuts import render
from rest_framework import generics
from .models import Artist
from .serializers import ArtistSerializer
import firebase_admin
from firebase_admin import credentials, firestore
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import random

json_content = {
    "type": "service_account",
    "project_id": "melodyhub-e6e1a",
    "private_key_id": "e4e945b0914512749763e6956a287c96ec7ee12a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCcdqw0J6+CsWTK\nuGMOsMPaaIPB+wV0QsUBXkp4MZmrAeAXtAt87ZiKvNrO0KOrmpM8eB2ZIduWWHgU\nSDyW3NDgZYoI3P37uo03wv9NIXSDQKjGqjtDx2scAFHLZfy+USc0ipmKu3gTwN3V\nnCXXLbsjbzrI7kDu7JJNstOyFnvhRo6XUXe1agxgpJnXMnrsAItBZiVHzU/fOmKR\nx3vKhLCDpCVpxmt9ZEh+o0W6b/Gxum/3H17ykZfi5pK/iPKkLXBZzy3NRuwIzbbV\nK0w69hDHA1KtnHq6L8MFyU07Xeh46G9IrqT+/XlOOTCR8vj10+MivM7DVvxtS60d\n9yauGpEZAgMBAAECggEAJNViKkAKdyG0SO358eAmp0DR/cVOriU21CDitqN0mdet\n7d6WksErV0Po3eWrli8kSMi9LQrVszHeCOZNjzVqHd2Bjp8Z0pxC+PTYncuJrol3\nAhfarlTgr/2aQ+AdTR91M48KYOjLtpjBkHM7TEoJg2jAxcMi+awrMAvwfr0AylIv\n2nI2IatZ69Rcn+i22IN+q22U3uwg7zqzgTJoQoOqQKKuIz2sEC7RDkw1kTPj4aA6\nJb+esRh1YH2VPc84EOFpGRT5CRy+k5ajNXI5z+quAyA1pbuu2PYFinCd2UOU5+lC\nZshWoD12wKeftT/jYMwp4x9Hbu9jwGog21rfJA7cdQKBgQDQSmbTQRwEBhSMZwEO\nzivGFwh6RmofsGHA6W1lxRQ1Zefjj9Dibm6wUnH2PWNmmMNj3aTcyAHCTZ6oaNyO\n/e+OIH0m30zYwCWQhES11DaHa1/FOFpzCewaP9IIvNT4fMiODRV9JAP8OenwzHao\nrTzS3aVNptAtij9JRrgBqQWALQKBgQDATUWx4lZHHzFPzSY9FY7ccDjeQb0w0N2f\nP8r/XnlkG/T3pRsAV+Q2qH6FChxEledmVRNxQjVcnPfgIJ1AEX2WpshpXaSG/TjG\n7yxuYpd/vL7Qe2VfJLQI8DV6XX/hB9UOnBHczvBlUgdv6N5SY0VWC/fGCPIacSPO\nclIKNgK8HQKBgQDJWKK9ZBso6JfEgW3MWhCGlI1lZdwAdgiI6x0NW82FMNVQbR2H\nRSlK2OfBGOaVruZyCzfrFIxev5m3Qmay81Y3FcDlasZmYJfvc2zYOCPeFDWn+Cm3\nOsg5N6hZOfDFpBpa9trm9YHEuFckpwGtXImHbSr2PWLQIuu6cdo+AJ2IoQKBgGES\n4NrSMdGHSoJJQkNVrZ9TuzFfKB0LYsTwFA5jZ44Emt2kaAP9WkPJPMz19J0euwgq\nbD0hOgS9bFekvxzHd4lkOgkOb26BR3cM53X1qRqfcgeWMu8bfRKCB8z0hAhZxtCw\nMkgv4qSTCxQQDqKyYB72vaYnf+efM38UsJtc9nZ1AoGBAIbvAU588vQyKTYXLdUu\n2wfXydDw8JdtMtSi+cL5ODRWsxjCWTMZI/EjxzZd9nSeYiqJx7rdDc1CIATZ3UYb\npYTwSKfeKfXu+MLXZUyRip89Q48KCLCu38cI1QXuuLr8BJ6DZ9WLoWTI8Xtt0ocB\npi3e/aPAppWA5SqYmXPdCLhf\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-6w7b4@melodyhub-e6e1a.iam.gserviceaccount.com",
    "client_id": "111364060463225682154",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6w7b4%40melodyhub-e6e1a.iam.gserviceaccount.com",
}


def get_credentials():
    return credentials.Certificate(json_content)


cred = get_credentials()
firebase_admin.initialize_app(cred)
db = firestore.client()


class get_all_artists(APIView):
    def get(self, request):
        artists_ref = firestore.client().collection("Artists")
        artists_data = []
        for artist in artists_ref.stream():
            artist_dict = artist.to_dict()
            artist_dict["artist_id"] = artist.id
            artists_data.append(artist_dict)
        return JsonResponse(artists_data, safe=False)


class get_artist_by_country(APIView):
    def get(self, request):
        country = request.query_params.get("country", None)
        artists_ref = (
            firestore.client().collection("Artists").where("country", "==", country)
        )
        artists_data = []
        for artist in artists_ref.stream():
            artist_dict = artist.to_dict()
            artist_dict["artist_id"] = artist.id
            artists_data.append(artist_dict)
        return JsonResponse(artists_data, safe=False)


class get_all_artist_country(APIView):
    def get(self, request):
        try:
            artists_ref = db.collection("Artists")
            artists_data = []
            for artist in artists_ref.stream():
                artist_dict = artist.to_dict()
                artist_dict["artist_id"] = artist.id
                artists_data.append(artist_dict)
            countries = []
            for artist in artists_data:
                country = artist.get("country", None)
                if country and country not in countries:
                    countries.append(country)
            return JsonResponse(countries, safe=False)
        except Exception as e:
            return JsonResponse(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def get_total_views_of_artist(artist_id):
    tracks_ref = db.collection("Tracks").where("artist_id", "==", artist_id)
    tracks_data = [track.to_dict() for track in tracks_ref.stream()]
    total_views = 0
    for track in tracks_data:
        total_views += track["view"]
    return total_views


class get_popular_artists(APIView):
    def get(self, request):
        limit = request.query_params.get("limit", None)
        try:
            limit = int(limit)
        except ValueError:
            return JsonResponse(
                {"error": "Invalid limit parameter"}, status=status.HTTP_400_BAD_REQUEST
            )
        artists_ref = db.collection("Artists")
        artists_data = artists_ref.stream()
        list_popular_artists = []
        for artist in artists_data:
            artist_dict = artist.to_dict()
            artist_dict["artist_id"] = artist.id
            artist_dict["total_views"] = get_total_views_of_artist(artist.id)
            list_popular_artists.append(artist_dict)
        list_popular_artists = sorted(
            list_popular_artists, key=lambda x: x["total_views"], reverse=True
        )
        return JsonResponse(list_popular_artists[:limit], safe=False)


class get_all_genres(APIView):
    def get(self, request):
        genres_ref = firestore.client().collection("Genres")
        genres_data = []
        for genre in genres_ref.stream():
            genre_dict = genre.to_dict()
            genre_dict["genre_id"] = genre.id
            genres_data.append(genre_dict)
        return JsonResponse(genres_data, safe=False)


class get_all_tracks(APIView):
    def get(self, request):
        tracks_ref = db.collection("Tracks")
        tracks_data = [track.to_dict() for track in tracks_ref.stream()]
        return JsonResponse(tracks_data, safe=False)


class get_shuffle_tracks(APIView):
    def get(self, request):
        limit = request.query_params.get("limit")
        try:
            limit = int(limit)
        except (TypeError, ValueError):
            return JsonResponse(
                {"error": "Invalid limit parameter"}, status=status.HTTP_400_BAD_REQUEST
            )
        tracks_ref = db.collection("Tracks").stream()
        track_ids = [track.id for track in tracks_ref]
        random.shuffle(track_ids)
        selected_track_ids = track_ids[:limit]
        selected_tracks = []
        for track_id in selected_track_ids:
            track_doc = db.collection("Tracks").document(track_id).get().to_dict()
            if track_doc:
                artist_doc = (
                    db.collection("Artists")
                    .document(track_doc["artist_id"])
                    .get()
                    .to_dict()
                )
                genre_doc = (
                    db.collection("Genres")
                    .document(track_doc["genres_id"])
                    .get()
                    .to_dict()
                )
                track_dict = {
                    "track_id": track_id,
                    "track_name": track_doc["track_name"],
                    "artist_name": (
                        artist_doc["artist_name"] if artist_doc else "Unknown"
                    ),
                    "genres_name": genre_doc["genre_name"] if genre_doc else "Unknown",
                }
                selected_tracks.append(track_dict)

        return JsonResponse(selected_tracks, safe=False)


class get_top_trending_tracks(APIView):
    def get(self, request):
        limit = request.query_params.get("limit", None)
        try:
            limit = int(limit)
        except ValueError:
            return JsonResponse(
                {"error": "Invalid limit parameter"}, status=status.HTTP_400_BAD_REQUEST
            )

        tracks_ref = (
            db.collection("Tracks")
            .order_by("view", direction=firestore.Query.DESCENDING)
            .limit(limit)
        )
        list_trending_tracks = []
        for track in tracks_ref.stream():
            track_dict = track.to_dict()
            track_dict["track_id"] = track.id
            artist_doc = (
                db.collection("Artists").document(track_dict["artist_id"]).get()
            )
            if artist_doc.exists:
                track_dict["artist_name"] = artist_doc.to_dict()["artist_name"]
            else:
                track_dict["artist_name"] = "Unknown"
            genre_doc = db.collection("Genres").document(track_dict["genres_id"]).get()
            if genre_doc.exists:
                track_dict["genres_name"] = genre_doc.to_dict()["genre_name"]
            else:
                track_dict["genres_name"] = "Unknown"
            list_trending_tracks.append(track_dict)
        return JsonResponse(list_trending_tracks, safe=False)


class get_tracks_by_artist_id(APIView):
    def get(self, request):
        artist_id = request.query_params.get("artist_id", None)
        if not artist_id:
            return JsonResponse({"error": "artist_id is required"}, status=400)
        tracks_ref = db.collection("Tracks").where("artist_id", "==", artist_id)
        list_tracks_by_artist_id = []
        for track in tracks_ref.stream():
            track_dict = track.to_dict()
            track_dict["track_id"] = track.id
            artist_doc = db.collection("Artists").document(artist_id).get()
            if artist_doc.exists:
                track_dict["artist_name"] = artist_doc.to_dict()["artist_name"]
            else:
                track_dict["artist_name"] = "Unknown"
            genre_doc = db.collection("Genres").document(track_dict["genres_id"]).get()
            if genre_doc.exists:
                track_dict["genres_name"] = genre_doc.to_dict()["genre_name"]
            else:
                track_dict["genres_name"] = "Unknown"
            list_tracks_by_artist_id.append(track_dict)
        list_tracks_by_artist_id = sorted(
            list_tracks_by_artist_id, key=lambda x: x["view"], reverse=True
        )
        return JsonResponse(list_tracks_by_artist_id, safe=False)


class get_tracks_by_genre_id(APIView):
    def get(self, request):
        genre_id = request.query_params.get("genre_id", None)
        if not genre_id:
            return JsonResponse({"error": "genre_id is required"}, status=400)
        tracks_ref = db.collection("Tracks").where("genres_id", "==", genre_id)
        tracks_data = [track.to_dict() for track in tracks_ref.stream()]
        list_tracks_by_genre_id = []
        for track in tracks_data:
            song = {
                "track_name": track.get("track_name", ""),
                "track_url": track.get("track_url", ""),
                "image_url": track.get("image_url", ""),
                "view": track.get("view", 0),
                "release_year": track.get("release_year", 2000),
                "duration": track.get("duration", 0),
                "artist_name": "",
                "genres_name": "",
            }

            artist_doc = db.collection("Artists").document(track["artist_id"]).get()
            if artist_doc.exists:
                song["artist_name"] = artist_doc.to_dict().get("artist_name", "Unknown")
            else:
                song["artist_name"] = "Unknown"
            genre_doc = db.collection("Genres").document(track["genres_id"]).get()
            if genre_doc.exists:
                song["genres_name"] = genre_doc.to_dict().get("genre_name", "Unknown")
            else:
                song["genres_name"] = "Unknown"
            list_tracks_by_genre_id.append(song)

        return JsonResponse(list_tracks_by_genre_id, safe=False)
