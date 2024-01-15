# your_app/views.py

from rest_framework import generics, permissions

from google.auth.transport import requests
from google.oauth2 import id_token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import  LoginSerializer, UserSerializer
import jwt
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import *
from datetime import datetime
import calendar
import random
import string

User = get_user_model()
verification_key_path = settings.PUBLIC_KEY_PATH
try:
    verification_key = open(settings.PUBLIC_KEY_PATH, 'r').read()
except FileNotFoundError:
    print(f"Error: Public key file not found at {settings.PUBLIC_KEY_PATH}")
   
def generate_random_string(length):
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        name = data.get("name")
        dob = data.get("dob")
        email = data.get("email")
        password = data.get("password")

        # Check if the email already exists
        if UserProfile.objects.filter(email=email).exists():
            return Response({"error": "An account with this email already exists."}, status=400)

        try:
            current_datetime = datetime.now()
            timestamp = calendar.timegm(current_datetime.utctimetuple())
            user = User.objects.create(username="dx"+str(timestamp)+"D", email=email)
            user.set_password(password)
            user.save()

            userProfile = UserProfile.objects.create(
                username=user,
                dx_user=True,
                dob=dob,
                name=name,
                email=email,
                secret_key=generate_random_string(60)
            )
            userProfile.save()
            return Response({"message": "Account created successfully."}, status=201)

        except Exception as e:
            user.delete()
            return Response({"error": str(e)}, status=500)


class GLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        token = data.get("token")
        id_info = id_token.verify_oauth2_token(token, requests.Request(), "439800211520-e23qodk9aeoq6k2pk3ss43g22aiv61hp.apps.googleusercontent.com")
        print(id_info)
        # # Check if the email already exists
        # if UserProfile.objects.filter(email=email).exists():
        #     return Response({"error": "An account with this email already exists."}, status=400)

        # try:
        #     current_datetime = datetime.now()
        #     timestamp = calendar.timegm(current_datetime.utctimetuple())
        #     user = User.objects.create(username="dx"+str(timestamp)+"D", email=email)
        #     user.set_password(password)
        #     user.save()

        #     userProfile = UserProfile.objects.create(
        #         username=user,
        #         dx_user=True,
        #         dob=dob,
        #         name=name,
        #         email=email,
        #         secret_key=generate_random_string(60)
        #     )
        #     userProfile.save()
        #     return Response({"message": "Account created successfully."}, status=201)

        # except Exception as e:
        #     user.delete()
        #      return Response({"error": str(e)}, status=500)
        return Response(id_info)



class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request,format=None):
        jwt_object = JWTAuthentication() 
        token = jwt_object.get_raw_token(jwt_object.get_header(request))  
        try:
            data = jwt.decode(token, verification_key, algorithms=["RS256"])
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError: {e}")
            print(f"Problematic token: {token}")
            print(data)

        userTrackData = UserTrack.objects.get(id=data["tk"])
        UserProfileData = UserProfile.objects.get(username=userTrackData.username)
        print(userTrackData,UserProfileData)

        success_data = {
            "name":UserProfileData.name,
            "dob":UserProfileData.dob,
            "email":UserProfileData.email,
            "phone_no":UserProfileData.phone_no,
            "profile_picture":UserProfileData.profile_picture.url if UserProfileData.profile_picture else None,
            "tfa":UserProfileData.tfa,
        }
        
        return Response(success_data)