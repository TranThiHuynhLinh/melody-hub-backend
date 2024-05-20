from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from .serializers import ArtistSerializer
import firebase_admin
from firebase_admin import credentials, firestore, auth
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import pyrebase
from .models import UserInfor
from .models import AccountRole
import jwt
import datetime
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
import requests

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

config = {
    "apiKey": "AIzaSyCstZCIJMvII4PhY7Yi91Ct9xwfPGv3GOI",
    "authDomain": "melodyhub-e6e1a.firebaseapp.com",
    "projectId": "melodyhub-e6e1a",
    "storageBucket": "melodyhub-e6e1a.appspot.com",
    "databaseURL": "https://melodyhub-e6e1a-default-rtdb.firebaseio.com",
}

FIREBASE_API_KEY = "AIzaSyCstZCIJMvII4PhY7Yi91Ct9xwfPGv3GOI"
FIREBASE_REST_API_URL = (
    "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key="
)


def get_credentials():
    return credentials.Certificate(json_content)


cred = get_credentials()
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    try:
        response = requests.post(
            FIREBASE_REST_API_URL + FIREBASE_API_KEY,
            data={"email": email, "password": password, "returnSecureToken": True},
        )
        if response.status_code == 200:
            data = response.json()
            user_id = data["localId"]
            AccountRole_ref = db.collection("AccountRole").document(user_id).get()
            token = jwt.encode(
                {
                    "user_id": user_id,
                    "username": AccountRole_ref.to_dict()["user_name"],
                    "role": AccountRole_ref.to_dict()["role_name"],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=168),
                },
                "SECRET_KEY",
                algorithm="HS256",
            )
            return Response({"token": token}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=401)
    except auth.UserNotFoundError:
        return JsonResponse({"message": "User not found"}, status=404)
    return JsonResponse({"message": "Invalid request method"}, status=400)


@api_view(["POST"])
def signup(request):
    email = request.data.get("email")
    password = request.data.get("password")
    name = request.data.get("username")
    try:
        user = authe.create_user_with_email_and_password(email, password)
        uid = user["localId"]
        AccountRole_ref = db.collection("AccountRole").document(uid)
        AccountRole_ref.set({"role_name": "user", "user_name": name})
        user_info_data = {
            "user_id": uid,
            "username": name,
            "avatar_image": "",
            "playlist_ids": [],
        }
        UserInfor_ref = db.collection("UserInfor").document(uid)
        UserInfor_ref.set(user_info_data)
        return Response({"message": "successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        error_message = str(e)
        if "EMAIL_EXISTS" in error_message:
            return Response(
                {"message": "failed", "error": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            return Response(
                {"message": "failed", "error": error_message},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ValidateTokenView(APIView):
    def get(self, request):
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                token = auth_header.split(" ")[1]
                payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
                return JsonResponse({"message": "Token is valid"}, status=200)
            except jwt.ExpiredSignatureError:
                return JsonResponse({"message": "Token expired"}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({"message": "Invalid token"}, status=401)
            except jwt.DecodeError:
                return JsonResponse({"message": "Error decoding token"}, status=401)
            except Exception as e:
                return JsonResponse({"message": f"Token error: {str(e)}"}, status=401)
        else:
            return JsonResponse({"message": "Authorization header missing"}, status=401)


@api_view(["POST"])
def change_account_role(request):
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        return JsonResponse(
            {"message": "Authorization header is missing"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    token = auth_header.split()[1]
    decoded_token = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
    user_id = decoded_token["user_id"]
    new_role = request.data.get("new_role")
    AccountRole_ref = db.collection("AccountRole").document(user_id)
    AccountRole_ref.update({"role_name": new_role})
    token = jwt.encode(
        {
            "user_id": user_id,
            "username": AccountRole_ref.to_dict()["user_name"],
            "role": new_role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=168),
        },
        "SECRET_KEY",
        algorithm="HS256",
    )
    return Response({"message": "Role updated successfully"}, status=status.HTTP_200_OK)
