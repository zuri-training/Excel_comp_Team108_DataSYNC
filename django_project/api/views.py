from django.shortcuts import render
from asyncio.log import logger
import applogger
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework.decorators import api_view, schema, permission_classes
from django.conf import settings
import datetime as dt
from datetime import date


@api_view(['GET'])
@permission_classes((AllowAny,))
def home(self):
    return Response({"status": 1, "message": "Home Page of Excel_comp(dataSyn) Project"})


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                status_code = status.HTTP_200_OK
                token_lifetime = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
                now = dt.datetime.now()
                login_date = str(now.strftime("%y-%m-%d %H:%M:%S"))
                new_time = now + token_lifetime
                expires_in = str(new_time.strftime("%y-%m-%d %H:%M:%S"))
                response = {
                    'status': 1,
                    'statusCode': status_code,
                    'message': 'User logged in successfully',
                    'token': serializer.data['access'],
                    'refresh_token': serializer.data['refresh'],
                    'login time': login_date,
                    'expires_in': expires_in,
                    'full_name': serializer.data['email'],

                }
                return Response(response, status=status_code)
        except:
            logger.exception('Invalid Manger Credential')
            return Response({'status': 0, 'message': 'Invalid Credential'}, status=status.HTTP_200_OK)




class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:

            serializer = self.serializer_class(data=request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                serializer.save()
                status_code = status.HTTP_201_CREATED

                response = {
                    'status': 1,
                    'statusCode': status_code,
                    'message': 'User successfully registered!',
                }

            return Response(response, status=status_code)
        except:
            logger.exception("Registration Unsuccessful")
            return Response({'status': 0, 'message': 'Registration Unsuccessful'}, status=status.HTTP_200_OK)


class UserLogOutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": 1, "message": "User logged Out Successfully"}, status=status.HTTP_200_OK)
        except:
            logger.exception("User not logged out")
            return Response({"status": 0, "message": "Logout Failed"}, status=status.HTTP_400_BAD_REQUEST)
