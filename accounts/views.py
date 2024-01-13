# your_app/views.py

from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
import jwt
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import *

User = get_user_model()
verification_key_path = settings.PUBLIC_KEY_PATH
try:
    verification_key = open(settings.PUBLIC_KEY_PATH, 'r').read()
except FileNotFoundError:
    print(f"Error: Public key file not found at {settings.PUBLIC_KEY_PATH}")
   
class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

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