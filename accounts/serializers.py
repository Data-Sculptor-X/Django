# your_app/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user,tk):
        token = super().get_token(user)
        token['tk'] = tk
        return token

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    remember_me = serializers.BooleanField(write_only=True, default=False)

    def validate(self, data):
        email = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        user_track = UserTrack(
            username=user,
           remember_me=data.get('remember_me', False),
           count= "1"
        )
        user_track.save()
        token = MyTokenObtainPairSerializer.get_token(user,user_track.id)
        success_data = {
            'refresh_token': str(token),
            'access_token': str(token.access_token)
        }

        return success_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


