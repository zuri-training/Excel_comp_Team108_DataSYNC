import email
from unittest.util import _MAX_LENGTH

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    email= serializers.EmailField(max_length=100, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=128, write_only=True)
    rpassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'rpassword',
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

    def validate(self, data):
        email = data['email']
        password = data['password']
        password = data['rpassword']
        
        if User.objects.filter(email=email, password=password) != []:
            return data
        else:
            raise serializers.ValidationError(
                "Email already exists!")
            
    def validate_password(self, data):
        if not data.get('password') or not data.get('rpassword'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('rpassword'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, allow_blank=False)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
        
        
