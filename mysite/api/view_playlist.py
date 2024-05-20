from django.shortcuts import render
from rest_framework import generics
from .models import Artist
from .serializers import ArtistSerializer
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import random
import jwt
import datetime

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
if not firebase_admin._apps:
    firebase_admin.initialize_app(
        cred, {"storageBucket": "gs://melodyhub-e6e1a.appspot.com"}
    )

db = firestore.client()
# bucket = storage.bucket()


class create_my_playlist(APIView):
    def post(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if auth_header is None:
                return JsonResponse(
                    {"message": "Authorization header is missing"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            token = auth_header.split()[1]
            decoded_token = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
            user_id = decoded_token["user_id"]
            playlist_name = request.data.get("playlist_name")
            playlist = db.collection("Playlists").document()
            playlist.set(
                {
                    "playlist_name": playlist_name,
                    "track_ids": [],
                    "recommended_track_ids": [],
                    "user_id": user_id,
                    "total_duration": 0,
                }
            )
            user = db.collection("UserInfor").document(user_id)
            user.update({"playlist_ids": firestore.ArrayUnion([playlist.id])})
            return JsonResponse(
                {"message": "successfully"}, status=status.HTTP_201_CREATED
            )
        except jwt.ExpiredSignatureError:
            return JsonResponse(
                {"message": "Token has expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.InvalidTokenError:
            return JsonResponse(
                {"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class remove_my_playlist(APIView):
    def post(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if auth_header is None:
                return JsonResponse(
                    {"message": "Authorization header is missing"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            token = auth_header.split()[1]
            decoded_token = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
            user_id = decoded_token["user_id"]
            playlist_id = request.data.get("playlist_id")
            user = db.collection("UserInfor").document(user_id)
            user.update({"playlist_ids": firestore.ArrayRemove([playlist_id])})
            playlist = db.collection("Playlists").document(playlist_id)
            playlist.delete()
            return JsonResponse(
                {"message": "successfully"}, status=status.HTTP_201_CREATED
            )
        except jwt.ExpiredSignatureError:
            return JsonResponse(
                {"message": "Token has expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.InvalidTokenError:
            return JsonResponse(
                {"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class get_my_playlist(APIView):
    def post(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if auth_header is None:
                return JsonResponse(
                    {"message": "Authorization header is missing"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            token = auth_header.split()[1]
            decoded_token = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
            user_id = decoded_token["user_id"]
            user = db.collection("UserInfor").document(user_id).get()
            playlist_ids = user.to_dict()["playlist_ids"]
            playlists = []
            for playlist_id in playlist_ids:
                playlist = db.collection("Playlists").document(playlist_id).get()
                playlist_dict = playlist.to_dict()
                playlist_dict["playlist_id"] = playlist_id
                playlists.append(playlist_dict)
            return JsonResponse(playlists, status=status.HTTP_200_OK, safe=False)
        except jwt.ExpiredSignatureError:
            return JsonResponse(
                {"message": "Token has expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.InvalidTokenError:
            return JsonResponse(
                {"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class get_tracks_by_playlist_id(APIView):
    def get(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return JsonResponse(
                    {"message": "Authorization header is missing"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            id_token = auth_header.split(" ")[1]
            try:
                decoded_token = jwt.decode(id_token, "SECRET_KEY", algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return JsonResponse(
                    {"message": "Token has expired"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            except jwt.InvalidTokenError:
                return JsonResponse(
                    {"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
                )
            playlist_id = request.query_params.get("playlist_id")
            if not playlist_id:
                return JsonResponse(
                    {"message": "playlist_id is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            playlist = db.collection("Playlists").document(playlist_id).get()
            if not playlist.exists:
                return JsonResponse(
                    {"message": "Playlist not found"}, status=status.HTTP_404_NOT_FOUND
                )

            playlist_data = playlist.to_dict()
            track_ids = playlist_data.get("track_ids", [])
            tracks = []

            for track_id in track_ids:
                track_data = db.collection("Tracks").document(track_id).get()
                if not track_data.exists:
                    continue

                track_dict = track_data.to_dict()
                track = {
                    "track_id": track_id,
                    "track_name": track_dict.get("track_name"),
                    "track_url": track_dict.get("track_url"),
                    "image_url": track_dict.get("image_url"),
                    "duration": track_dict.get("duration"),
                    "release_year": track_dict.get("release_year"),
                    "view": track_dict.get("view"),
                }

                artist_id = track_dict.get("artist_id")
                genre_id = track_dict.get("genres_id")

                if artist_id:
                    artist_data = db.collection("Artists").document(artist_id).get()
                    if artist_data.exists:
                        track["artist_name"] = artist_data.to_dict().get("artist_name")

                if genre_id:
                    genre_data = db.collection("Genres").document(genre_id).get()
                    if genre_data.exists:
                        track["genres_name"] = genre_data.to_dict().get("genre_name")

                tracks.append(track)

            return JsonResponse(tracks, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class get_tracks_recommend_by_playlist_id(APIView):
    def get(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return JsonResponse(
                    {"message": "Authorization header is missing"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            id_token = auth_header.split(" ")[1]
            try:
                decoded_token = jwt.decode(id_token, "SECRET_KEY", algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return JsonResponse(
                    {"message": "Token has expired"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            except jwt.InvalidTokenError:
                return JsonResponse(
                    {"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
                )
            playlist_id = request.query_params.get("playlist_id")
            if not playlist_id:
                return JsonResponse(
                    {"message": "playlist_id is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            playlist = db.collection("Playlists").document(playlist_id).get()
            if not playlist.exists:
                return JsonResponse(
                    {"message": "Playlist not found"}, status=status.HTTP_404_NOT_FOUND
                )

            playlist_data = playlist.to_dict()
            track_ids = playlist_data.get("recommended_track_ids", [])
            tracks = []

            for track_id in track_ids:
                track_data = db.collection("Tracks").document(track_id).get()
                if not track_data.exists:
                    continue

                track_dict = track_data.to_dict()
                track = {
                    "track_id": track_id,
                    "track_name": track_dict.get("track_name"),
                    "track_url": track_dict.get("track_url"),
                    "image_url": track_dict.get("image_url"),
                    "duration": track_dict.get("duration"),
                    "release_year": track_dict.get("release_year"),
                    "view": track_dict.get("view"),
                }

                artist_id = track_dict.get("artist_id")
                genre_id = track_dict.get("genres_id")

                if artist_id:
                    artist_data = db.collection("Artists").document(artist_id).get()
                    if artist_data.exists:
                        track["artist_name"] = artist_data.to_dict().get("artist_name")

                if genre_id:
                    genre_data = db.collection("Genres").document(genre_id).get()
                    if genre_data.exists:
                        track["genres_name"] = genre_data.to_dict().get("genre_name")

                tracks.append(track)

            return JsonResponse(tracks, status=status.HTTP_200_OK, safe=False)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class add_track_to_my_playlist(APIView):
    def post(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return JsonResponse(
                    {"message": "Authorization header is missing"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            id_token = auth_header.split(" ")[1]
            try:
                decoded_token = jwt.decode(id_token, "SECRET_KEY", algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return JsonResponse(
                    {"message": "Token has expired"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            except jwt.InvalidTokenError:
                return JsonResponse(
                    {"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
                )
            playlist_id = request.data.get("playlist_id")
            track_id = request.data.get("track_id")

            if not playlist_id or not track_id:
                return JsonResponse(
                    {"message": "playlist_id and track_id are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            playlist_ref = db.collection("Playlists").document(playlist_id)
            playlist = playlist_ref.get()

            if not playlist.exists:
                return JsonResponse(
                    {"message": "Playlist not found"}, status=status.HTTP_404_NOT_FOUND
                )

            playlist_data = playlist.to_dict()
            track_ids = playlist_data.get("track_ids", [])
            if track_id not in track_ids:
                track_ids.append(track_id)
                batch = db.batch()
                batch.update(playlist_ref, {"track_ids": list(track_ids)})
                batch.commit()

                update_total_duration_of_playlist(playlist_ref, track_id, "add")
                update_recommended_track_ids(playlist_ref, track_id, "add")
            else:
                return JsonResponse(
                    {"message": "Track already exists in playlist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return JsonResponse(
                {"message": "successfully"}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class remove_track_from_my_playlist(APIView):
    def post(self, request):
        try:
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return JsonResponse(
                    {"message": "Authorization header is missing"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            id_token = auth_header.split(" ")[1]
            try:
                decoded_token = jwt.decode(id_token, "SECRET_KEY", algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return JsonResponse(
                    {"message": "Token has expired"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            except jwt.InvalidTokenError:
                return JsonResponse(
                    {"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
                )
            playlist_id = request.data.get("playlist_id")
            track_id = request.data.get("track_id")

            if not playlist_id or not track_id:
                return JsonResponse(
                    {"message": "playlist_id and track_id are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            playlist_ref = db.collection("Playlists").document(playlist_id)
            playlist = playlist_ref.get()

            if not playlist.exists:
                return JsonResponse(
                    {"message": "Playlist not found"}, status=status.HTTP_404_NOT_FOUND
                )

            playlist_data = playlist.to_dict()
            track_ids = playlist_data.get("track_ids", [])
            if track_id in track_ids:
                track_ids.remove(track_id)
                batch = db.batch()
                batch.update(playlist_ref, {"track_ids": list(track_ids)})
                batch.commit()
                update_total_duration_of_playlist(playlist_ref, track_id, "remove")
                update_recommended_track_ids(playlist_ref, track_id, "remove")
            else:
                return JsonResponse(
                    {"message": "Track does not exist in playlist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return JsonResponse(
                {"message": "successfully"}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def update_recommended_track_ids(playlist_ref, track_id, action):
    try:
        track_ref = db.collection("Tracks").document(track_id)
        track = track_ref.get().to_dict()
        playlist = playlist_ref.get().to_dict()
        if action == "add":
            artist_id = track["artist_id"]
            genre_id = track["genres_id"]
            recommended_track_ids = playlist["recommended_track_ids"]

            tracks = (
                db.collection("Tracks").where("artist_id", "==", artist_id).stream()
            )
            i = 0
            for track in tracks:
                track_data = track.to_dict()
                if (
                    i < 1
                    and track.id != track_id
                    and track.id not in recommended_track_ids
                ):
                    recommended_track_ids.append(track.id)
                    i += 1

            # Thêm các bản ghi từ cùng một thể loại
            tracks = db.collection("Tracks").where("genres_id", "==", genre_id).stream()
            j = 0
            for track in tracks:
                track_data = track.to_dict()
                if (
                    j < 1
                    and track.id != track_id
                    and track.id not in recommended_track_ids
                ):
                    recommended_track_ids.append(track.id)
                    j += 1

            # Update Firestore với batch writes
            batch = db.batch()
            batch.update(playlist_ref, {"recommended_track_ids": recommended_track_ids})
            batch.commit()
        elif action == "remove":
            recommended_track_ids = playlist.get("recommended_track_ids", [])
            recommended_track_ids = recommended_track_ids[2:]
            batch = db.batch()
            batch.update(playlist_ref, {"recommended_track_ids": recommended_track_ids})
            batch.commit()

    except Exception as e:
        print(f"Error updating recommended track ids: {str(e)}")


def update_total_duration_of_playlist(playlist_ref, track_id, action):
    track_ref = db.collection("Tracks").document(track_id)
    track = track_ref.get().to_dict()
    playlist = playlist_ref.get().to_dict()
    if action == "add":
        duration = track["duration"]
        batch = db.batch()
        batch.update(playlist_ref, {"total_duration": firestore.Increment(duration)})
        batch.commit()
    elif action == "remove":
        duration = track["duration"]
        batch = db.batch()
        batch.update(playlist_ref, {"total_duration": firestore.Increment(-duration)})
        batch.commit()
