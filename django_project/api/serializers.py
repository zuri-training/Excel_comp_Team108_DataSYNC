import email
from unittest.util import _MAX_LENGTH

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())]
                                   )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 
                  'last_name', 'password', 'password2',)
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    def validate(self, data):
        email = data['email']
        password = data['password']
        
        if User.objects.filter(email=email, password=password) != []:
            return data
        else:
            raise serializers.ValidationError(
                "Email already exists!")
            
    def Validate_Password(self, data):
        if not data.get('password') or not data.get('password2'):
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
        
        
